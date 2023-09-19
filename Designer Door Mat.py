#!/bin/python3

n, m = input().split()
n = int(n)
m = int(m)


def row(separator: str) -> str:
    dashes = (m - len(separator)) // 2
    right = dashes + len(separator)
    left = dashes + right
    return separator.rjust(right, "-").ljust(left, "-")


sep = ".|."
middle_line_number = n // 2

for i in range(n):
    if i < middle_line_number:
        print(row(sep))
        sep = sep + (2 * ".|.")

    elif i > middle_line_number:
        sep = sep.replace(".|.", "", 2)
        print(row(sep))

    else:
        print(row("WELCOME"))
