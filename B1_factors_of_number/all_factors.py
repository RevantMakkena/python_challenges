def factors(num):
    number = 1
    all_nums = []
    while number < num:
        if num % number == 0:
            all_nums.append(number)
        number += 1
    return num == sum(all_nums)
    print(sum(all_nums))


factors(24)
