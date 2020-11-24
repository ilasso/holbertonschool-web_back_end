#!/usr/bin/env python3
"""
"""
from client import GithubOrgClient

a = GithubOrgClient('ilasso')

print(dir(a))
print(a.ORG_URL)
print(type(a.org))
x = a.org
print(x)
print(a._public_repos_url)
