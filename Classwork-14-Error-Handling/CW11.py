# INPUT
config = {}

try:
    archivo = open("config.txt", "r")

    for linea in archivo:
        clave, valor = linea.strip().split("=")
        config[clave] = float(valor)

    archivo.close()

except FileNotFoundError:
    print("No se encontró el archivo config.txt")
    raise SystemExit

except ValueError:
    print("El archivo config.txt tiene un formato incorrecto")
    raise SystemExit

except OSError:
    print("No fue posible leer el archivo")
    raise SystemExit

else:
    try:
        ancho = int(config["ancho"])
        alto = int(config["alto"])
        max_iter = int(config["max_iter"])

        if ancho <= 0 or alto <= 0 or max_iter <= 0:
            raise ValueError("Los valores deben ser mayores que cero")

    except KeyError:
        print("Faltan parámetros en config.txt")
        raise SystemExit

    except ValueError as e:
        print(e)
        raise SystemExit


# PROCESS
try:
    salida = open("clase.csv", "w")

    salida.write("fila,columna,iteraciones\n")

    for fila in range(alto):
        for columna in range(ancho):

            real = config["real_min"] + (columna / ancho) * (
                config["real_max"] - config["real_min"]
            )

            imag = config["imag_min"] + (fila / alto) * (
                config["imag_max"] - config["imag_min"]
            )

            c = complex(real, imag)

            z = 0 + 0j
            iteraciones = 0

            while abs(z) <= 2 and iteraciones < max_iter:
                z = z * z + c
                iteraciones += 1

            salida.write(f"{fila},{columna},{iteraciones}\n")

    salida.close()

except KeyError:
    print("Faltan valores de configuración")
    raise SystemExit

except OSError:
    print("No fue posible crear el archivo de salida")
    raise SystemExit

# OUTPUT
else:
    print("DONE")