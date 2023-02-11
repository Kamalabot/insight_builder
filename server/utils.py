"""Module takes care of the password encryption and decryption process"""
from passlib.context import CryptContext

passwd = CryptContext(schemes=["bcrypt"],deprecated='auto')

def hasher(password: str):
    """Plain password to hashed"""
    return passwd.hash(password)

def verify_pass(plain_pass:str, hash_pass:str):
    """just verify, not return any pass"""
    return passwd.verify(plain_pass, hash_pass)
