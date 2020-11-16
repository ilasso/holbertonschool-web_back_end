#!/usr/bin/env python3
""" Auth: Hash password"""
import bcrypt
from db import DB
from typing import TypeVar
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> str:
    """ method that takes in a password
        string arguments and returns a string
        The returned string is a salted hash of
        the input password, hashed with bcrypt.hashpw
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def _generate_uuid() -> str:
    """
    return a string representation of a new UUID
    """
    return str(uuid.uuid4())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        constructor
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ hash the password with _hash_password
            save the user to the database using self._db
            return the User object
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            user = None
            passw = _hash_password(password)
            return self._db.add_user(email, passw)
        if user:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """
        login validation
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                passwhash = _hash_password(password)
                return bcrypt.checkpw(password.encode('utf-8'),
                                      user.hashed_password)
        except NoResultFound:
            return False
