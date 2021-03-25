def linearSearch(elements, target):
    for i in elements:
        if i == target:
            return True
    return False


linearSearch([1, 2, 3, 4], 10)
