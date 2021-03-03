div, mod = divmod(100, 10)
digits = [mod, ]
while div:
    div, mod = divmod(div, 10)
    digits.append(mod)

print(digits)
