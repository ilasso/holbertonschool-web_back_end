#!/usr/bin/env python3
""" Base module
"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """
    auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path[len(path)-1] == '/':
            path = path[:-1]
        for i in excluded_paths:

            exclude = i[:-1]
            if exclude == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization_header
        """
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user
        """
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if not request:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
