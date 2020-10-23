#!/usr/bin/env python3
from typing import Generator


def generate() -> Generator[int, None, None]:
    for i in range(10):
        yield i

for i in generate():
    print(i)

"""l = [i for i in generate()]
print(l)"""
