def slices(series, length):

    if(len(series) < length) or length <= 0:
        raise ValueError(
            "length shouldn't be bigger than length")

    result = []
    start = 0
    while start <= len(series):
        if length > len(series):
            break
        result.append(series[start:length])
        start += 1
        length += 1
    return result


print(slices("", 1))
