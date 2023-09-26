x, y = map(int, input().split())

equation = input().replace("x", f"{x}")

print(eval(equation) == y)
