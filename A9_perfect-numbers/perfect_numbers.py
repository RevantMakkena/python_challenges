def classify(number):
    if number < 1:
        raise ValueError("number should be greater than 0")
    factor = 1
    all_nums = []
    while factor < number:
        if number % factor == 0:
            all_nums.append(factor)
        factor += 1

    return (('abundant', 'perfect')[sum(all_nums) == number], 'deficient')[sum(all_nums) < number]

    # if number == sum(all_nums):
    #     return "perfect"
    # elif number < sum(all_nums):
    #     return "abundant"
    # else:
    #     return "deficient"


print(classify(6))
