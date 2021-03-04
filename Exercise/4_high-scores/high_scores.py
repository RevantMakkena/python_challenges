def latest(scores):
    # print(scores[-1])
    # print(scores[len(scores)-1])
    return scores[len(scores)-1]


def personal_best(scores):
    # max(scores) is also same
    return sorted(scores, reverse=True)[0]


def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]


# print(personal_best([10, 1, 2, 18, 39, 22]))
# print(personal_top_three([10, 1, 2, 18, 39, 22]))
# print(latest([10, 1, 2, 18, 39, 22]))
