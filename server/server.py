"""The main server running the API"""
#main server
from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .table_models import Base
from .database_orm import get_db, engine
#bring in the response, request object schema
from . import users, bikers

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )
app.include_router(users.router)
app.include_router(bikers.router)

@app.get('/',status_code=status.HTTP_200_OK)
def base_route():
    return {"message":"InsightBuilder collective"}


