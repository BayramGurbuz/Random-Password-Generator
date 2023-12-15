                         # Random Password Generator
import random

def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return "".join(temp_list)

# Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter1 = chr(random.randint(65, 90))
# Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2 = chr(random.randint(65, 90))

# Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter1 = chr(random.randint(97, 122))
# Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter2 = chr(random.randint(97, 122))

# Generate a random digit (based on ASCII code)
digit1 = chr(random.randint(48, 57))
# Generate a random digit (based on ASCII code)
digit2 = chr(random.randint(48, 57))

# Generate a random punctuation sign (based on ASCII code)
punc1 = chr(random.randint(33, 47) or random.randint(58, 64))
# Generate a random punctuation sign (based on ASCII code)
punc2 = chr(random.randint(33, 47) or random.randint(58, 64))

password = (uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 +
            digit1 + digit2 + punc1 + punc2)

password = shuffle(password)

print(password)
