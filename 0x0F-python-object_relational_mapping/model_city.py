#!/usr/bin/python3
"""a Python file similar to model_state.py named model_city.py that contains the class definition of a City."""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
