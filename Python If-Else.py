#!/bin/python3

import math
import os
import random
import re
import sys


def solve(n: int):
    if n % 2 != 0:
        print("Weird")
    else:
        if n in range(6, 21):
            print("Weird")
        else:
            print("Not Weird")


if __name__ == "__main__":
    n = int(input().strip())

    solve(n)
