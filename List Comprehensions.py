#!/bin/python3


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

grid_of_3d = []
row = [0, 0, 0]

for i in range(x + 1):
    row[0] = i

    for j in range(y + 1):
        row[1] = j

        for k in range(z + 1):
            row[2] = k

            if sum(row) != n:
                grid_of_3d.append(row.copy())

print(grid_of_3d)
