# Enter your code here. Read input from STDIN. Print output to STDOUT


t = int(input())

while t > 0:
    try:
        a, b = list(map(int, input().split()))
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

    t -= 1
