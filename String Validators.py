has = {
    "alnum": False,
    "alpha": False,
    "digit": False,
    "lower": False,
    "upper": False,
}


def validate(s: str) -> None:
    for char in s:
        if char.isalnum():
            has["alnum"] = True

        if char.isalpha():
            has["alpha"] = True

        if char.isdigit():
            has["digit"] = True

        if char.islower():
            has["lower"] = True

        if char.isupper():
            has["upper"] = True


if __name__ == "__main__":
    s = input()

    validate(s)

    print(has["alnum"])
    print(has["alpha"])
    print(has["digit"])
    print(has["lower"])
    print(has["upper"])
