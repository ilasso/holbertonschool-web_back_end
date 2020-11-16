#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)
sessionid = auth.create_session(email)
print(sessionid)
user = auth.get_user_from_session_id(sessionid)
print(f"userid={user.id}, email={user.email}, sessionid={user.session_id}")
auth.destroy_session(user.id)
print(f"userid={user.id}, email={user.email}, sessionid={user.session_id}")
