a = int(input())
set_a = set(map(int, input().split()))


n = int(input())

while n > 0:
    order = input().split()
    tmp_set = set(map(int, input().split()))

    if order[0] == "intersection_update":
        set_a.intersection_update(tmp_set)
    elif order[0] == "update":
        set_a.update(tmp_set)
    elif order[0] == "symmetric_difference_update":
        set_a.symmetric_difference_update(tmp_set)
    elif order[0] == "difference_update":
        set_a.difference_update(tmp_set)

    n -= 1

print(sum(set_a))
