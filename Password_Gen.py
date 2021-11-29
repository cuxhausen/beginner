import random
import string

length = int(input('Write the length of your password: '))

def gen(length, method=["lowercase", "uppercase", "digits", "punctuation"]):
    """String.lowercase, uppercase, digits, punctuation."""
    pwd = []
    for i in range(length):
        choice = random.choice(method)
        if choice == "lowercase":
            pwd.append(random.choice(string.ascii_lowercase))
        if choice == "uppercase":
            pwd.append(random.choice(string.ascii_uppercase))
        if choice == "digits":
            pwd.append(random.choice(string.digits))
        if choice == "punctuation":
            pwd.append(random.choice(string.punctuation))
        if choice == "string":
            pwd.append(random.choice(string.punctuation))

    random.shuffle(pwd)
    return ''.join(pwd)

print(gen(length))
