#!/usr/bin/env python3
""" Database module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base
from user import User
from typing import TypeVar


class DB:
    """
        class to map db tables in a python object class
    """
    def __init__(self):
        """
        constructor
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """
            create session conect
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> TypeVar('User'):
        """ Add a user instance to the session DB """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs: dict) -> object:
        """ returns the first row found in the users table
            as filtered by the method’s input arguments
        """
        obj = self._session.query(User).filter_by(**kwargs).first()
        if not obj:
            raise NoResultFound
        return obj
