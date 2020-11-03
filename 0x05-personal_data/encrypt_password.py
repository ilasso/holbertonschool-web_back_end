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
