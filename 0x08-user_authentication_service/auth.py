#!/usr/bin/env python3
""" Auth: Hash password"""
import bcrypt


def _hash_password(password: str) -> str:
    """ method that takes in a password
        string arguments and returns a string
        The returned string is a salted hash of
        the input password, hashed with bcrypt.hashpw
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
