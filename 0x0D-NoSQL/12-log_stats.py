#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def getlog(a: dict) -> int:
    """count log"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    return nginx_logs.count_documents(a)


def print_resume():
    """
    print resume data
    """
    print(f"{getlog({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {getlog({'method': 'GET'}) }")
    print(f"\tmethod POST: {getlog({'method': 'POST'}) }")
    print(f"\tmethod PUT: {getlog({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {getlog({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {getlog({'method': 'DELETE'})}")
    print(f"{getlog({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    print_resume()
