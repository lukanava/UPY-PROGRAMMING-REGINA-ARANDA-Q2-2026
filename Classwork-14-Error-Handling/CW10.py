# INPUT
usuarios = {
    'jperez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno', 'nombre': 'Ana Martín'},
    'cgarcia': {'password': '1234', 'rol': 'alumno', 'nombre': 'Carlos García'},
    'lmendez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Laura Méndez'},
    'rlopez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Roberto López'},
    'msantos': {'password': '1234', 'rol': 'alumno', 'nombre': 'María Santos'},
    'mlopez': {'password': '1234', 'rol': 'maestro', 'nombre': 'María López'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}

materias = ('Matemáticas', 'Programación', 'Inglés')

calificaciones = {
    'jperez': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 6.0},
    'amartin': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'cgarcia': {'Matemáticas': 8.0, 'Programación': 8.5, 'Inglés': 7.5},
    'lmendez': {'Matemáticas': 8.5, 'Programación': 6.0, 'Inglés': 8.0},
    'rlopez': {'Matemáticas': 7.5, 'Programación': 8.0, 'Inglés': 8.5},
    'msantos': {'Matemáticas': 3.0, 'Programación': 8.5, 'Inglés': 8.0}
}

# PROCESS

while True:
    try:
        apodo = input("Usuario: ").strip()
        contraseña = input("Contraseña: ")

        if apodo == "":
            raise ValueError("Debe escribir un usuario")

        if apodo not in usuarios:
            raise KeyError

        if contraseña != usuarios[apodo]["password"]:
            raise PermissionError

    except ValueError as e:
        print(e)

    except KeyError:
        print("Usuario incorrecto")

    except PermissionError:
        print("Contraseña incorrecta")

    else:
        print("Bienvenido", usuarios[apodo]["nombre"])
        break

rol = usuarios[apodo]["rol"]

if rol == "alumno":

    aprobadas = set()

    print("Boleta de", usuarios[apodo]["nombre"])

    try:
        for materia in materias:
            print(materia, calificaciones[apodo][materia])

            if calificaciones[apodo][materia] >= 7:
                aprobadas.add(materia)

    except KeyError:
        print("No se encontraron las calificaciones del alumno")
        raise SystemExit

    pendientes = set(materias) - aprobadas

    print("Aprobadas:", aprobadas)
    print("Pendientes:", pendientes)

elif rol == "maestro":

    print("Rol:", usuarios[apodo]["rol"])

    print("Alumnos:")

    for usuario in calificaciones:
        print("-", usuarios[usuario]["nombre"])
        print()

    print("\nMaterias:")

    for materia in materias:
        print("-", materia)

    cambio = input("¿Quieres cambiar la calificación de un alumno? (si/no) ")

    while cambio.lower() == "si":

        try:
            alumno = input("Alumno: ").strip()
            materia = input("Materia: ").strip()

            if alumno not in calificaciones:
                raise KeyError("Alumno no encontrado")

            if materia not in materias:
                raise ValueError("Materia no encontrada")

            nueva = float(input("Nueva calificación: "))

            if nueva < 0 or nueva > 10:
                raise ValueError("La calificación debe estar entre 0 y 10")

        except KeyError as e:
            print(e)

        except ValueError as e:
            print(e)

        else:
            seguridad = input("¿Estás seguro (si/no)? ")

            if seguridad.lower() == "si":
                calificaciones[alumno][materia] = nueva

                print("Calificaciones actualizadas de", usuarios[alumno]["nombre"])

                for materia in materias:
                    print(materia, calificaciones[alumno][materia])

        cambio = input("¿Quieres cambiar otra calificación? (si/no) ")

elif rol == "coordinador":

    print("Maestros:")

    try:
        for usuario, datos in usuarios.items():

            if datos["rol"] == "maestro":
                print(datos["nombre"])

    except KeyError:
        print("Error al leer la información de maestros")

    print()
    print("-" * 60)
    print(f"{'Alumno':20}|{'Matemáticas':12}|{'Programación':12}|{'Inglés':8}")
    print("-" * 60)

    try:
        for alumno, notas in calificaciones.items():

            print(
                f"{usuarios[alumno]['nombre']:20}|"
                f"{notas['Matemáticas']:12}|"
                f"{notas['Programación']:12}|"
                f"{notas['Inglés']:8}"
            )

            print("-" * 60)

    except KeyError:
        print("Error al mostrar las calificaciones")