t = int(input())

while t > 0:
    a = int(input())
    set_a = set(map(int, input().split()))

    b = int(input())
    set_b = set(map(int, input().split()))

    # Solution 1
    # -----------

    # is_subset = True

    # for item_a in set_a:
    #     if item_a not in set_b:
    #         is_subset = False
    #         break

    # is_subset = True

    # ======================

    # Solution 2
    # -----------

    is_subset = set_a.issubset(set_b)

    print(is_subset)

    t -= 1
