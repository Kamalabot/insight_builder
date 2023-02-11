"""This file contains the users and login end point"""

from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from . import table_models
from .schema import res_user, create_user
from typing import List
from .oauth import get_current_user, verify_access_token, create_access_token
from .table_models import Base, User
from .utils import hasher, verify_pass
from .database_orm import get_db
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
        prefix='/user',
        tags=['Authentication']
        )

@router.post("/create_user",status_code=status.HTTP_201_CREATED,
          response_model=res_user)
def creating_user(user_get:create_user,db:Session = Depends(get_db)):
    """Takes new user and password, and stores the details in the
    database. The hasher and verifier in the utils module take care of the
    safe encryption and decryption of the password"""

    user_get.pass_phrase = hasher(user_get.pass_phrase)
    new_user = User(**user_get.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/v1/show_users",status_code=status.HTTP_200_OK,
         response_model=List[res_user])
def list_users(db: Session = Depends(get_db)):
    data_users = db.query(User).all()
    return data_users

@router.get("/id/{user_id}",response_model=res_user)
def locate_user(user_id:int, db:Session = Depends(get_db)):
    one_user = db.query(User).filter(User.user_id == user_id).first()
    if one_user == None:
        raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Id is invalid"))
    return one_user

@router.post("/login")
def login(user_cred: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    user_enter = db.query(User).filter(User.email_id == user_cred.username).first()

    if not user_enter:
        raise(HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail="User id not located"))
    
    verifying = verify_pass(user_cred.password, user_enter.pass_phrase)

    if not verifying:
        raise(HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail='Wrong pass. please re-enter.'))

    get_token = create_access_token(data = {"user_id":user_enter.user_id})

    return {"access_token":get_token, "token_type":"bearer"}

@router.post("/validate")
def validate_user(token: str, db: Session = Depends(get_db)):
   get_id = verify_access_token(token,HTTPException(status_code = status.HTTP_401_UNAUTHORIZED))
   return get_id
