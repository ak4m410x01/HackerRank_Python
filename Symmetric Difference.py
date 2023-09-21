n1 = int(input())
s1 = set(map(int, input().split()))

n2 = int(input())
s2 = set(map(int, input().split()))

s3 = sorted(s1.symmetric_difference(s2))

for item in s3:
    print(item)
