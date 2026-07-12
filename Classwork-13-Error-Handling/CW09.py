class InvalidEndingError(Exception):
    pass
try:

    verb = input("Verbo a conjugar ").lower().strip()
    if verb == "":
        raise ValueError("Ingresa un  verbo")
    if verb.isalpha()==False:
        raise ValueError("El verbo solo debe contener letras")
    if verb[-2:] not in ["ar", "er", "ir"]:
        raise InvalidEndingError("El verbo debe tterminar en:'ar','er' o 'ir' ")
except InvalidEndingError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    pronouns = ['Yo', 'Tu', 'El', 'Nosotros', 'Vosotros', 'Ellos']
    endings = {
        'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
        'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
        'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
    }
    stem = verb[:-2]
    ending = verb[-2:]
    ending_list = endings[ending]
    for index, pronoun in enumerate(pronouns):
        end = ending_list[index]
        print(f"{pronoun} {stem}{end}")

