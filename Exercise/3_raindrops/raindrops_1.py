drops = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))


def raindrops(n):
    """Converts a number to a string according to the raindrop sounds."""

    speak = [s for f, s in drops if n % f == 0]
    return speak if speak else str(n)


# print(type(drops))
# print([f for f, s in drops])
print(raindrops(7))
