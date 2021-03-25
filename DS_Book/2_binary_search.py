def binarySearch(nums, target):
    left, right = 0, len(nums)

    while left < right:
        middle = (left+right)//2

        if nums[middle] < target:
            left = middle+1
        else:
            right = middle

    return left


binarySearch([1, 2, 3, 4, 10, 11, 17, 28, 33, 66], 17)
