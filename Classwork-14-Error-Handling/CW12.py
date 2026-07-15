from PIL import Image

# INPUT
config = {}

try:
    archivo = open("config.txt", "r")

    for linea in archivo:
        clave, valor = linea.strip().split("=")
        config[clave] = float(valor) if "." in valor else int(valor)

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
        with open("clase.csv", "r") as data:
            datos = data.readlines()

    except FileNotFoundError:
        print("No se encontró el archivo clase.csv")
        raise SystemExit

    except OSError:
        print("No fue posible leer el archivo clase.csv")
        raise SystemExit

# PROCESS
try:
    alto = config["alto"]
    ancho = config["ancho"]
    max_iter = config["max_iter"]

    if alto <= 0 or ancho <= 0 or max_iter <= 0:
        raise ValueError("Los valores de configuración deben ser mayores que cero")

    img = Image.new("HSV", (ancho, alto))
    encabezados = datos.pop(0)

    for dato in datos:
        fila, columna, iteraciones = map(int, dato.strip().split(","))

        brillo = (
            0
            if iteraciones == max_iter
            else int((iteraciones / max_iter) * 255)
        )

        img.putpixel((columna, fila), (brillo, 255, 255))

    img_rgb = img.convert("RGB")
    img_rgb.save("mandelbrot-clase.png")

except KeyError:
    print("Faltan parámetros en config.txt")
    raise SystemExit

except ValueError as e:
    print(e)
    raise SystemExit

except IndexError:
    print("El archivo clase.csv está vacío")
    raise SystemExit

except OSError:
    print("No fue posible guardar la imagen")
    raise SystemExit

# OUTPUT
else:
    print("DONE")