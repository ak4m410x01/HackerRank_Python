cube = lambda x: pow(x, 3)  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])

    return series[0:n]


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
