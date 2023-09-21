def is_integer(func):

    def wrapper(value):

        if isinstance(value, int):
            return func(value)

        else:
            return "not integer!"

    return wrapper

@is_integer
def is_odd(x):
    return x % 2 == 1

print(is_odd(9))
