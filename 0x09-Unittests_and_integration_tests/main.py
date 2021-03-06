#!/usr/bin/env python3
""" test access_nested_map"""
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch
import json

class MyClass:
    """
    to test
    """
    @memoize
    def a_method(self):
        print("a_method called")
        return 4223

print("test access_nested_map")
nested_map = {"a": {"b": {"c": "hola"}}}
print(nested_map)
print(access_nested_map(nested_map, ["a","b","c"]))
nested_map = {"a": 1}
print(nested_map)
print(access_nested_map(nested_map, ("a",)))

nested_map = {"a": {"b": 2}}
print(nested_map)
print(access_nested_map(nested_map, ("a",)))
nested_map =  {"a": {"b": 2}}
print(nested_map)
print(access_nested_map(nested_map, ("a","b")))

print("test get_json whitout mock")
a = get_json("https://swapi-api.hbtn.io/api/planets/1/")
print(f"a={a}")
print("B test get_json whitout mock")



print("test memoize")

my_object = MyClass()
# first call do not memoize
print("first call")
print(my_object.a_method)
print("end first call")
# second call, not excecute only rem the result. makes memoize
print("second call")
print(my_object.a_method)
print("end second call")
print("third call")
print(my_object.a_method)
print("END third call")
