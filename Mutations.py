def mutate_string(string, position, character):
    ans = ""
    for i in range(len(string)):
        if i == position:
            ans += character
            continue

        ans += string[i]

    return ans


if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
