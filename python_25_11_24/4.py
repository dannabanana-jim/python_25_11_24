#Ejercicio 4
#Escribir un programa que le diga al usuario que ingrese una cadena.
#  El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

# Programa que solicita al usuario una cadena y cuenta cuántas letras mayúsculas contiene.
def contar_mayusculas(cadena):
    # Usamos una expresión generadora para contar las letras mayúsculas.
    return sum(1 for char in cadena if char.isupper())

# Solicitar al usuario que ingrese una cadena.
cadena_usuario = input("Ingresa una cadena: ")

# Contamos las letras mayúsculas en la cadena ingresada.
cantidad_mayusculas = contar_mayusculas(cadena_usuario)

# Mostramos el resultado al usuario.
print(f"La cadena ingresada tiene {cantidad_mayusculas} letras mayúsculas.")
