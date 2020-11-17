#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth
from db import DB

email = 'bob@bob.com'
password = 'MyPwdOfBob'

auth = Auth()
my_db = DB()

user = my_db.add_user(email, password)
print(user.id)

print(auth.get_reset_password_token(email))
