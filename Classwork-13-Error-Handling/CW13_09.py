class InvalidEndingError(Exception):
    pass


# INPUT
try:

    verb = input("Verb to conjugate: ").lower().strip()
    if verb == "":
        raise ValueError("You must enter a verb.")
    if not verb.isalpha():
        raise ValueError("The verb must contain only letters.")
    if verb[-2:] not in ["ar", "er", "ir"]:
        raise InvalidEndingError("The verb must end in 'ar', 'er', or 'ir'.")

# PROCESS
    pronouns = ['Yo', 'Tu', 'El', 'Nosotros', 'Vosotros', 'Ellos']

    endings = {
        'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
        'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
        'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
    }

    stem = verb[:-2]
    ending = verb[-2:]
    ending_list = endings[ending]

# OUTPUT
    for index, pronoun in enumerate(pronouns):
        end = ending_list[index]
        print(f"{pronoun} {stem}{end}")

except InvalidEndingError as e:
    print(e)

except ValueError as e:
    print(e)

