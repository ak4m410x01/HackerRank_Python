def solve(N):
    l = []
    while N > 0:
        order = input().split()

        if order[0] == "insert":
            e = int(order[1])
            i = int(order[2])
            l.insert(e, i)

        elif order[0] == "print":
            print(l)

        elif order[0] == "remove":
            e = int(order[1])
            if e in l:
                l.remove(e)

        elif order[0] == "append":
            e = int(order[1])
            l.append(e)

        elif order[0] == "sort":
            l.sort()

        elif order[0] == "pop":
            if len(l):
                l.pop()

        elif order[0] == "reverse":
            l.reverse()

        N -= 1


if __name__ == "__main__":
    N = int(input())

    solve(N)
