#!/usr/bin/env python3
""" encript_password:
    Functions to encrypt passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
     expects one string argument name password and returns a salted,
     hashed password, which is a byte string.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    function that expects 2 arguments and returns a boolean.
    Arguments:

    hashed_password: bytes type
    password: string type
    Use bcrypt to validate that the provided password matches
    the hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
