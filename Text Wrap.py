import textwrap


def wrap(string, max_width):
    wraped_string = ""
    putnewline = 1

    for char in string:
        wraped_string += char
        if putnewline % max_width == 0:
            wraped_string += "\n"

        putnewline += 1

    return wraped_string


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
