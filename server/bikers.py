"""This file contains the get endpoints """
from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from schema import biker_row,delivery_dimensions, pickup_dimensions, features_ds, prediction_fm
from table_models import Base,Bikers, deliverydimensions, pickupdimensions, featuresds, predictionfm 
from typing import List
from database_orm import get_db
from sqlalchemy.orm import Session

router = APIRouter(
        prefix='/biker',
        tags=['Analysis']
        )
@router.get('/v1/bikers',status_code=status.HTTP_200_OK,
                    response_model=List[biker_row])
def query_biker(db: Session = Depends(get_db)):
    biker_detail = db.query(Bikers).limit(2).all()
    return biker_detail

@router.get('/v1/deliveryd',status_code=status.HTTP_200_OK,
                    response_model=List[delivery_dimensions])
def delivery_detail(db: Session = Depends(get_db)):
    delivery_detail = db.query(deliverydimensions).limit(2).all()
    return delivery_detail

@router.get('/v1/pickupd',status_code=status.HTTP_200_OK,
                    response_model=List[pickup_dimensions])
def pickup_biker(db: Session = Depends(get_db)):
    pickup_detail = db.query(pickupdimensions).\
                    filter(pickupdimensions.IntervalPickup.isnot(None)).\
                    limit(2).all()
    return pickup_detail

@router.get('/v1/features',status_code=status.HTTP_200_OK,
                    response_model=List[features_ds])
def feature_biker(db: Session = Depends(get_db)):
    feature_detail = db.query(featuresds).limit(2).all()
    return feature_detail
 
@router.get('/v1/predict',status_code=status.HTTP_200_OK,
                    response_model=List[prediction_fm])
def predict_biker(db: Session = Depends(get_db)):
    predict_detail = db.query(predictionfm).limit(2).all()
    return predict_detail

