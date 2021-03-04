"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
ONES = "1 * num of ones"
TWOS = "2 * num of twos"
THREES = "3 * num of threes"
FOURS = "4 * num of fours"
FIVES = "5 * num of fives"
SIXES = "6 * num of sixes"
CHOICE = "Sum of the dice"
YACHT = 50  # All five dice showing the same face
FULL_HOUSE = "total"  # Three of one number and two of another
FOUR_OF_A_KIND = "total of 4"  # At least four dice showing the same face
LITTLE_STRAIGHT = 30  # 1-2-3-4-5
BIG_STRAIGHT = 30  # 2-3-4-5-6


def score(dice, category):
    if category == ONES:
        return sum([x for x in dice if x == 1])
    elif category == TWOS:
        return sum([x for x in dice if x == 2])
    elif category == THREES:
        return sum([x for x in dice if x == 3])
    elif category == FOURS:
        return sum([x for x in dice if x == 4])
    elif category == FIVES:
        return sum([x for x in dice if x == 5])
    elif category == SIXES:
        return sum([x for x in dice if x == 6])
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        return ((0, 50)[len(set(dice)) == 1])
    elif category == FULL_HOUSE:
        return (0, sum(dice))[len(set(dice)) == 2]
    elif category == FOUR_OF_A_KIND:
        pass
    elif category == LITTLE_STRAIGHT:
        return (0, 30)[sum([val if dice[idx] == idx+1 else 0 for idx, val in enumerate(sorted(dice))]) == 15]
    else:
        return (0, 30)[sum([val if dice[idx] == idx+2 else 0 for idx, val in enumerate(sorted(dice))]) == 15]
