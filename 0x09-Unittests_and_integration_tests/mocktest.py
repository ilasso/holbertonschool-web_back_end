#!/usr/bin/env python3
from unittest import mock
from unittest.mock import Mock, patch
from test_utils import get_json
import os.path
import requests
import json
# MagicMock implements most magic methods such as __getitem__,
# __contains__,__len__,etc
m = mock.Mock()
#m = mock.MagicMock()
"""print(m.foo())
print(m.a.b.c)
print(m[0])
print('foo' in m)"""
""" the default return value is a new Mock.object
    same to MacigMock
"""
print(m())
print(m.return_value)
"""
"""
print(os.path.getsize('/etc/hosts'))
patcher = mock.patch('os.path.getsize')
mock_getsize = patcher.start()
print(mock_getsize)
print(os.path.getsize)
mock_getsize.return_value = 10
print(os.path.getsize('/etc/hosts'))
patcher.stop()
print(os.path.getsize('/etc/hosts'))

with mock.patch('os.path.getsize') as mock_getsize:
    mock_getsize.return_value = 10
    print(os.path.getsize('/etc/hosts'))

print(os.path.getsize('/etc/hosts'))

print("decorator")
# when the function return the patch is undone
@mock.patch('os.path.getsize')
def f(mock_getsize):
    mock_getsize.return_value = 10
    return os.path.getsize('/etc/hosts')

print(os.path.getsize('/etc/hosts'))
print(f())
print(os.path.getsize('/etc/hosts'))
print(f())


print("test get_json whidth mock")

response = Mock()
response.json.return_value = {"a":"b"}
patcher = patch('requests.get',return_value=response)
mock_getsize = patcher.start()
print(get_json('https://swapi-api.hbtn.io/api/planets/1/'))
response.json.return_value = {"a":"c"}
print(get_json('https://swapi-api.hbtn.io/api/planets/1/'))
patcher.stop()
#real
print(get_json('https://swapi-api.hbtn.io/api/planets/1/'))
