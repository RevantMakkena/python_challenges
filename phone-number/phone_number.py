class PhoneNumber:
    def __init__(self, number):
        self.raw_phone_number = number
        self.phone_digits = None
        self.number = self.formattedNumber()
        self.area_code = self.number[:3]

    def formattedNumber(self):
        self.phone_digits = [
            val for val in self.raw_phone_number if val.isdigit()]

        if len(self.phone_digits) >= 10 and int(self.phone_digits[0]) == 1:
            self.phone_digits.pop(0)

        for idx, val in enumerate(self.phone_digits):
            if (idx == 0 or idx == 3) and not 2 <= int(val) <= 9:
                raise ValueError("Values should be in between 2 and 9")

            if idx > 10:
                raise ValueError("Numbers should be 10")

            if idx == len(self.phone_digits)-1 and idx != 9:
                raise ValueError("Not enough digits")

        return ''.join(self.phone_digits)

    def pretty(self):
        return f"({''.join(self.phone_digits[:3])})-{''.join(self.phone_digits[3:6])}-{''.join(self.phone_digits[6:10])}"


# x = PhoneNumber("123456789")
# print(x.pretty())
