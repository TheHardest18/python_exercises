titulo = "Proporciona los siguientes datos del libro:"
nombre = input("Introduzca nombre del libro: ")
id = int(input("Introduzca ID del libro: "))
precio = float(input("Introduzca precio del libro: "))
envio = input("Indica si el envio es gratiuito (True/False)")

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = "Valor incorrecto debe introducir True/False"

# print(f"Nombre: {nombre}\nID: {id}\nPrecio: {precio}\nEnvio Gratuito?: {envio}")
# F String puedes poner texto preformateado
print(f'''
Nombre: {nombre}
ID: {id}
Precio: {precio}
Envio Gratuito?: {envio}
''')

