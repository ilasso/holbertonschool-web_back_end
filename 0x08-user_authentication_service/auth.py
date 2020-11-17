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

    def create_session(self, email: str) -> str:
        """returns the session ID as a string."""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """Find user by session ID"""
        if session_id:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except NoResultFound:
                return None
        return None

    def destroy_session(self, user_id: int) -> None:
        """updates the corresponding user’s session ID to None"""
        if user_id:
            self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ If it exists, generate a UUID and
            update the user’s reset_token database field
            Return: the token
        """
        if email:
            try:
                user = self._db.find_user_by(email=email)
            except Exception:
                raise ValueError
            resettoken = _generate_uuid()
            self._db.update_user(user.id, reset_token=resettoken)
            return resettoken

    def update_password(self, reset_token: str, password: str) -> None:
            """ update the user’s hashed_password field with the new
                hashed password and the reset_token field to None
            """
            try:
                user = self._db.find_user_by(reset_token=reset_token)
                hashed_password = _hash_password(password)
                self._db.update_user(user.id,
                                     hashed_password=hashed_password,
                                     reset_token=None)
                return None
            except Exception:
                raise ValueError
