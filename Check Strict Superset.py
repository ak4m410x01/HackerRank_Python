a = set(map(int, input().split()))

n = int(input())

is_superset = True

while n > 0:
    tmp = set(map(int, input().split()))

    if not a.issuperset(tmp):
        is_superset = False
        break
    n -= 1

print(is_superset)
