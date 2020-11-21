#!/usr/bin/env python3
from utils import access_nested_map


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
