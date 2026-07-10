from PIL import Image

config ={}

archivo=open("config.txt","r")

for linea in archivo:
    clave, valor = linea.strip().split("=")
    config[clave]=float(valor) if "." in valor else int(valor)
archivo.close()

print(config)

with open("clase.csv") as data:
    datos=data.readline() #quitar encabezados
    
alto,ancho=config['alto'], config['ancho']
img=Image.new('HSV', (ancho, alto))

