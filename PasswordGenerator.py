import random

# Set Constants
SPECIAL_CHARACTERS = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

# Set Password Length, Convert to Integer
length = int(input('Enter Password Length: '))

# Length Validation
while length < 4 or length > 64:

    print('The length of password must be at least 4! Try again.')
    length = input('Enter Password Length: ')

# Build Password
password_character_arr = []

for i in range(length):

    # Upper Case Character
    if (i % 4 == 0): 
        random_upper_case_character = chr(random.randint(65, 90))
        password_character_arr.append(random_upper_case_character)

    # Lower Case Character
    elif (i % 4 == 1):
        random_lower_case_character = chr(random.randint(97, 122))
        password_character_arr.append(random_lower_case_character)

    # Digit Character
    elif (i % 4 == 2):
        random_digit_character = chr(random.randint(48, 57))
        password_character_arr.append(random_digit_character)

    # Special Character
    else:
        random_special_character = SPECIAL_CHARACTERS[random.randint(0, len(SPECIAL_CHARACTERS) - 1)]
        password_character_arr.append(random_special_character)

# print(password_character_arr) <- debug use

# Reshuffle Password Characters
random.shuffle(password_character_arr)

# Join Array Elements into String
password_final = ''.join(password_character_arr)

# Display Password
print(f'Generated Password: {password_final}')