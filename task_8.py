'''
Your job is to write a function which
increments a string, to create a new string.

If the string already ends with a number,
the number should be incremented by 1.
If the string does not end with a number.
the number 1 should be appended to the new string.
Examples:

foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100

Attention: If the number has leading zeros
the amount of digits should be considered
'''


# VERS 1
def increment_string(string):
    text = ''.join(filter(str.isalpha, string))
    numbers = string[len(text):]

    if numbers == '':
        return text + '1'

    numbers_int = int(numbers)
    new_numbers = str(numbers_int + 1).rjust(len(numbers), '0')
    return text + new_numbers


#  VERS 2
# def increment_string2(string):
#     # Extract text and numbers parts
#     text = ''.join(filter(str.isalpha, string))
#     numbers = string[len(text):]
#
#     if numbers.isdigit():
#         # If there are leading zeros, handle them
#         if numbers.startswith('0'):
#             new_numbers = str(int(numbers) + 1).zfill(len(numbers))
#         else:
#             new_numbers = str(int(numbers) + 1)
#
#         new_string = text + new_numbers
#     else:
#         new_string = text + '1'
#
#     return new_string


if __name__ == '__main__':
    example = 'foo099'  # ['foo', 'foobar23', 'foo0042', 'foo9','foo099']
    increment_string(example)
    print(increment_string(example))
