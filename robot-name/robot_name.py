from random import choice, random, sample
import string


class Robot:
    def __init__(self):
        self.name = self.genName()

    def getLetters(self):
        return sample(string.ascii_uppercase, 2)

    def getRandomDigits(self):
        return sample(string.digits, 3)

    def genName(self):
        return f"{''.join(self.getLetters())}{''.join(self.getRandomDigits())}"

    def reset(self):
        self.name = str()
        self.name = self.genName()


x = Robot()
print(x.name)
print(x.reset())
