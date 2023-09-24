t = int(input())

while t > 0:
    a = int(input())
    set_a = set(map(int, input().split()))

    b = int(input())
    set_b = set(map(int, input().split()))

    is_subset = True

    for item_a in set_a:
        if item_a not in set_b:
            is_subset = False
            break

    print(is_subset)

    t -= 1
