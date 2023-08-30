import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(30), nullable=False)
    username = Column(String(250), nullable=False)



class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer)
    gender = Column(String(10))
    created = Column(Integer)
    updated = Column(Integer)
    eye_color = Column(String(20))
    hair_color = Column(String(15))
    height = Column(Integer)
    skin_color = Column(String(15))
    mass = Column(Integer)
    person_url = Column(String(30))
    planet_url = Column(String(50), ForeignKey('planet.planet_url'))


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table planet
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = (Integer)
    diameter = Column(Integer)
    created = Column(Integer)
    updated = Column(Integer)
    gravity = Column(String(20))
    orbital_period = Column(Integer)
    surface_water = Column(Integer)
    rotation_period = Column(String(15))
    population = Column(Integer)
    terrain = Column(String(20))
    person_url = Column(String(30), ForeignKey('characters.characters_url'))
    planet_url = Column(String(50))


class Favorite(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table favorite.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')