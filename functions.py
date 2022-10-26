import random


def passwordGenerator(lowercase_include: bool,
                      uppercase_include: bool,
                      special_include: bool,
                      numbers_include: bool,
                      length: int):

    # Variables
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    special = ['!', '@', '#', '$', '%', '&']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    initial = []

    # Options add to chosen
    if lowercase_include:
        initial = initial + lowercase
    if uppercase_include:
        initial = initial + uppercase
    if special_include:
        initial = initial + special
    if numbers_include:
        initial = initial + numbers

    # Password Generation
    password = ''.join([str(item) for item in random.choices(initial, k=length)])
    return password
