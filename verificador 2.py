class DigitoVerificadorError(Exception):
    pass
check=True
while check:
    try:
        rol = input("Ingrese el rol: ")
        rol_sin_digito, digito = rol.split("-")
        check=False
    except ValueError:
        print("Rol incorrecto")

try:
    numerical = rol [:]
    invertido = rol_sin_digito[::-1]
    if not invertido.isnumeric():
        raise ValueError (f"{invertido} tiene caracteres no numericos")
    if not numerical.isnumeric():
        raise ValueError (f"{numerical} tiene caracteres no numericos \n Intente de nuevo")
except ValueError as e:
    print(e)
secuencia =[2,3,4,5,6,7]
suma=0

for index in range (len(invertido)):
    multiplicando=secuencia[index % 6]
    numero=int(invertido[index:index+1])
    suma+=numero * multiplicando
    
total=suma%11
verificador= 11- total

try:
    if verificador != int(digito):
        raise DigitoVerificadorError(f"El dgito verificador no coincide, {verificador}")
except DigitoVerificadorError as e:
    print(e)
else:
    print(f"{rol_sin_digito}-{verificador}")