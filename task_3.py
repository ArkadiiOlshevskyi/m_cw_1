'''
The Case:
Your website has a large audience in
Scandinavia and surrounding countries.
Marketing thinks it would be great to
welcome visitors to the site in their
own language. Luckily you already use
an API that detects the user's location,
so this is an easy win.
The Task:
 - Think of a way to store the languages as a database (eg an object).
 - Write a 'welcome' function that takes a parameter 'language' (always a string),
 and returns a greeting - if you have it in your database.
 It should default to English if the language is not in the database,
 or in the event of an invalid input.
Possible invalid inputs include:
IP_ADDRESS_INVALID - not a valid ipv4 or ipv6 ip address
IP_ADDRESS_NOT_FOUND - ip address not in the database
IP_ADDRESS_REQUIRED - no ip address was supplied


'''

database = {'english': 'Welcome',
'czech': 'Vitejte',
'danish': 'Velkomst',
'dutch': 'Welkom',
'estonian': 'Tere tulemast',
'finnish': 'Tervetuloa',
'flemish': 'Welgekomen',
'french': 'Bienvenue',
'german': 'Willkommen',
'irish': 'Failte',
'italian': 'Benvenuto',
'latvian': 'Gaidits',
'lithuanian': 'Laukiamas',
'polish': 'Witamy',
'spanish': 'Bienvenido',
'swedish': 'Valkommen',
'welsh': 'Croeso'}


def greet(language):
    lowercase_language = language.lower()
    # Check if the language is in the database
    if lowercase_language in database:
        return database[lowercase_language]
    elif lowercase_language == "":
        return "IP_ADDRESS_REQUIRED - no ip address was supplied"
    else:
        return "Welcome"  # Default to English if language not found


def main():
    language = input("Enter the user's preferred language: ")
    print(greet(language))

if __name__ == '__main__':
    main()
