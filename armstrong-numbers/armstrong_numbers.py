def is_armstrong_number(number):
    given_str = str(number)
    total_digits = len(given_str)
    final_sum = 0

    for i in given_str:
        final_sum += int(i) ** total_digits

    if number == final_sum:
        return True
    return False


print(is_armstrong_number(10))


# %% Attempt 2

def is_armstrong(number):
    exp = len(str(number))
    return number == sum((int(a) ** exp for a in str(number)))
