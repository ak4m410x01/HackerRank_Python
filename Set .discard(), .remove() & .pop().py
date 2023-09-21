n = int(input())
s = set(map(int, input().split()))

N = int(input())

while N > 0:
    operation = input().split()

    if len(operation) > 1:
        operation[1] = int(operation[1])

    if operation[0] == "remove":
        if operation[1] in s:
            s.remove(operation[1])

    elif operation[0] == "discard":
        s.discard(operation[1])

    else:
        if len(s):
            s.pop()

    N -= 1

print(sum(s))
