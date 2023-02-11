from pydantic import BaseModel, EmailStr
from typing import Optional

class biker_row(BaseModel):
    ID :str
    Delivery_person_ID :str
    Delivery_person_Age :float
    Delivery_person_Ratings :float
    Restaurant_latitude :float
    Restaurant_longitude :float
    Delivery_location_latitude :float
    Delivery_location_longitude :float
    Order_Date :str
    Time_Orderd :str
    Time_Order_picked :str
    Weather :str
    Road_traffic_density :str
    Vehicle_condition :int
    Type_of_order :str
    Type_of_vehicle :str
    multiple_deliveries :float
    Festival :str
    City :str
    Name :str
    rowNum :int
    class Config:
        orm_mode = True

class prediction_fm(BaseModel):
    label:int
    prediction:int 
    class Config:
        orm_mode = True

class pickup_dimensions(BaseModel):
    pick_ID: str
    Time_Order_picked: str
    Time_orderd: str
    IntervalPickup: int
    class Config:
        orm_mode = True

class features_ds(BaseModel):
    DeliveryPersonID: float
    TypeOfVehicle: float 
    DeliveryPersonAge: float
    DeliveryPersonRatings: float
    Restaurant_latitude: float
    Restaurant_longitude: float
    Delivery_location_latitude: float
    Delivery_location_longitude: float
    Weather_idx: float 
    Type_of_order_idx: float 
    multiple_deliveries_idx: float 
    IntervalPickup:int
    class Config:
        orm_mode = True

class delivery_dimensions(BaseModel):
    ID: str
    Delivery_person_ID: str
    Type_of_Vehicle: str
    DeliveryPersonAge: float
    DeliveryPersonRatings: float
    TypeOfVehicle: float
    DeliveryPersonID: float
    class Config:
        orm_mode = True

class create_user(BaseModel):
    email_id:EmailStr
    pass_phrase:str

class res_user(BaseModel):
    email_id:EmailStr
    user_id:str
    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    email_id:EmailStr
    password:str

class Token(BaseModel):
    access_token: str
    token_typ: str

class TokenData(BaseModel):
    id: Optional[str] = None
