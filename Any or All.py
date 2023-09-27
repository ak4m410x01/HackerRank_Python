# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

numbers = list(map(int, input().split()))

condition_1 = all([number > 0 for number in numbers])
condition_2 = any([str(number) == str(number)[::-1] for number in numbers])

print(all([condition_1, condition_2]))
