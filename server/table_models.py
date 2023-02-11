"""The module provides the schema for the database tables"""
from sqlalchemy import Column, Integer, Float, String
from .database_orm import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(Base):
    __tablename__ = 'user_table'
    user_id = Column(Integer, primary_key=True,nullable=False)
    email_id = Column(String, nullable=False, unique=True)
    pass_phrase = Column(String, nullable=False)

class Bikers(Base):
    """Bikers Class provides access to the bikers_table in the database"""
    __tablename__ = 'bikers_table'
    ID = Column(String)
    Delivery_person_ID = Column(String)
    Delivery_person_Age= Column(Float)
    Delivery_person_Ratings= Column(Float)
    Restaurant_latitude= Column(Float)
    Restaurant_longitude= Column(Float)
    Delivery_location_latitude= Column(Float)
    Delivery_location_longitude= Column(Float)
    Order_Date= Column(String)
    Time_Orderd= Column(String)
    Time_Order_picked= Column(String)
    Weather= Column(String)
    Road_traffic_density= Column(String)
    Vehicle_condition= Column(Integer)
    Type_of_order= Column(String)
    Type_of_vehicle= Column(String)
    multiple_deliveries= Column(Float)
    Festival= Column(String)
    City= Column(String)
    Name= Column(String)
    rowNum= Column(Integer,primary_key=True)

class predictionfm(Base):
    __tablename__ = 'predictionfm'
    label=Column(Integer,primary_key=True)
    prediction=Column(Integer) 

class pickupdimensions(Base):
    __tablename__ = 'pickupdimensions'
    pick_ID= Column(String,primary_key=True)
    Time_Order_picked= Column(String)
    Time_orderd= Column(String)
    IntervalPickup= Column(Integer)

class featuresds(Base):
    __tablename__ = 'featuresds'
    DeliveryPersonID= Column(Float,primary_key=True)
    TypeOfVehicle= Column(Float) 
    DeliveryPersonAge= Column(Float)
    DeliveryPersonRatings= Column(Float)
    Restaurant_latitude= Column(Float)
    Restaurant_longitude= Column(Float)
    Delivery_location_latitude= Column(Float)
    Delivery_location_longitude= Column(Float)
    Weather_idx= Column(Float) 
    Type_of_order_idx= Column(Float) 
    multiple_deliveries_idx= Column(Float) 
    IntervalPickup=Column(Integer)

class deliverydimensions(Base):
    __tablename__ = 'deliverydimensions'
    ID= Column(String,primary_key=True)
    Delivery_person_ID= Column(String)
    Type_of_Vehicle= Column(String)
    DeliveryPersonAge= Column(Float)
    DeliveryPersonRatings= Column(Float)
    TypeOfVehicle= Column(Float) 
    DeliveryPersonID= Column(Float) 

