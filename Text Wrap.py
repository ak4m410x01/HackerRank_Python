import textwrap


def wrap_user_method(string, max_width):
    wraped_string = ""
    putnewline = 1

    for char in string:
        wraped_string += char
        if putnewline % max_width == 0:
            wraped_string += "\n"

        putnewline += 1

    return wraped_string


def wrap_builtin_method(string, max_width):
    wraped_string = textwrap.wrap(string, max_width)
    return "\n".join(wraped_string)


def wrap(string, max_width):
    # return wrap_user_method
    return wrap_builtin_method(string, max_width)


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
