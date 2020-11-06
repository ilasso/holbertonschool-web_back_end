#!/usr/bin/env python3
""" Base module
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64


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
