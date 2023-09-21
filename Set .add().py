numbers = int(input())
store = set()

while numbers > 0:
    country = input()
    store.add(country)
    numbers -= 1

print(len(store))
