#!/usr/bin/env python3
""" API authentication
"""
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar
import uuid
from models.user import User


class SessionAuth(Auth):
    """ Session Auth class"""
    pass
