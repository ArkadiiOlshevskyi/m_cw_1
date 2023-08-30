'''
Write a function that accepts an array
of 10 integers (between 0 and 9),
that returns a string of those numbers
in the form of a phone number.

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
'''


# Example 1
def create_phone_number(n):
    a = ''.join(map(str, n[:3]))
    b = ''.join(map(str, n[3:6]))
    c = ''.join(map(str, n[6:]))
    return f"({a}) {b}-{c}"


# Example 2
def create_phone_number(n):
    return '({}) {}-{}'.format(''.join(map(str, n[:3])), ''.join(map(str, n[3:6])), ''.join(map(str, n[6:])))


# Example 3
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


# Example 4
def create_phone_number(n):
    n = ''.join(map(str, n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])


if __name__ == '__main__':
    phone_number = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    contact = create_phone_number(phone_number)
    print(contact)
