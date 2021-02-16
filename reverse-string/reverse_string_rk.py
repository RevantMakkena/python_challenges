# %%

def reverse(string):
    total_len = len(string)
    reverse_string = ""
    for i in reversed(range(total_len)):
        reverse_string += string[i]
    print(reverse_string)


reverse("hello")

# %%


def reverse(input):
    print(input[::-1])  # Last one is step
    print(input[::2])


reverse("hello")

# %%


def reverse(input):
    print(''.join(reversed(input)))


reverse("hello")

# %%  recursion


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


reverse("I'm hungry!")
# %%  Stack


def reverse(str):
    reversed = []
    reverse_str = ""
    for i in str:
        reversed.append(i)

    for i in range(len(str)):
        reverse_str += reversed.pop()

    print(reverse_str)


reverse("Hello, wassup!!")

# %%
