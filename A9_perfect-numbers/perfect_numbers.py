def classify(number):
    if number <= 0:
        return ValueError("number should be greater than 0")
    factor = 1
    all_nums = []
    while factor < number:
        if number % factor == 0:
            all_nums.append(factor)
        factor += 1

    if number == sum(all_nums):
        return "perfect"
    elif number < sum(all_nums):
        return "abundant"
    else:
        return "deficient"
