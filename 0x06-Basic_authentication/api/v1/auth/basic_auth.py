#!/usr/bin/env python3
""" Base module
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


class BasicAuth(Auth):
    """
    BasicAuth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        extract_base64_authorization_header
        """
        if not authorization_header:
            return None
        if type(authorization_header) is not str:
            return None
        spauthheader = authorization_header.split(' ')
        if spauthheader[0] != "Basic":
            return None
        return spauthheader[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        decode_base64_authorization_header
        """
        if not base64_authorization_header:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            b64bytes = base64_authorization_header.encode('utf-8')
            bytes = base64.b64decode(b64bytes)
            return bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        extract_user_credentials:
        returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        user, email = decoded_base64_authorization_header.split(":")
        return user, email

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        user_object_from_credentials:
        returns the User instance based on his email and password.
        """
        if user_email is None:
            return None
        if type(user_email) is not str:
            return None
        if user_pwd is None:
            return None
        if type(user_pwd) is not str:
            return None
        try:
            useremail = User.search({"email": user_email})
        except Exception:
            return None
        if not useremail:
            return None
        for i in useremail:
            if i.is_valid_password(user_pwd):
                return i
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user:
        overloads Auth and retrieves the User instance for a request
        """
        try:
            header = self.authorization_header(request)
            b64auheader = self.extract_base64_authorization_header(header)
            decb64auh = self.decode_base64_authorization_header(b64auheader)
            credentials = self.extract_user_credentials(decb64auh)
            return self.user_object_from_credentials(credentials[0],
                                                     credentials[1])
        except Exception:
            return None
