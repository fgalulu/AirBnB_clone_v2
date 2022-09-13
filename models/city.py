#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, string, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60, ForeignKey('state.id'), nullable=false)
        name = Column(String(128), nullable=false)
    else:
        state_id = ""
        name = ""
