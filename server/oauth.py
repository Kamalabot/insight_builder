from jose import JWTError, jwt
from database_orm import get_db
import table_models
from schema import TokenData
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta

#openssl rand -hex 32
secret_key = '3bc83d63c81731bd3f25c1f58d01ec6e78957c49a720fa220bd58318965fe8ee'
algo = 'HS256'
expiration = 21

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login',auto_error=False)
Depends(oauth2_scheme)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(expiration))
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode, secret_key, algorithm=algo)
    return encode_jwt

def verify_access_token(token:str, cred_exception):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algo])
        id = payload.get("user_id")
        if id is None:
            raise cred_exception
        token_data = TokenData(id = id)
    except JWTError:
        raise cred_exception
    return token_data

def get_current_user(token:str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    cred_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
                                   detail = 'not validated',
                                   headers={"WWW-Authenticate":"Bearer"})
    token = verify_access_token(token, cred_exception)
    user = db.query(table_models.User).filter(table_models.User.user_id==token.id).first()
    return user.user_id
