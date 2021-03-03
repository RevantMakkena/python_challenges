def is_armstrong_number(number):
    given_str = str(number)
    total_digits = len(given_str)
    final_sum = 0

    for i in given_str:
        final_sum += int(i) ** total_digits

    return number == final_sum


print(is_armstrong_number(10))


# %%  3
def is_armstrong_number(number):
    return number == sum([int(n) ** len(str(number)) for n in str(number)])


is_armstrong_number(1022)

# %% Attempt 2


def is_armstrong(number):
    exp = len(str(number))
    return number == sum((int(a) ** exp for a in str(number)))
