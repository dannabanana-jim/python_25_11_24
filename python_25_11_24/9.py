#Ejercicio 9
#Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" 
#tiene y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

# Función que cuenta cuántas veces aparece cada vocal en una palabra
def contar_vocales(palabra):
    # Creamos un diccionario para almacenar las cuentas de cada vocal
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Convertimos la palabra a minúsculas para que no haya distinción entre mayúsculas y minúsculas
    palabra = palabra.lower()
    
    # Recorremos cada letra de la palabra
    for letra in palabra:
        if letra in vocales:
            vocales[letra] += 1
    
    return vocales

# Pedir al usuario que ingrese una palabra
palabra_usuario = input("Ingresa una palabra para contar las vocales: ")

# Llamamos a la función contar_vocales() pasando la palabra ingresada
resultado_vocales = contar_vocales(palabra_usuario)

# Mostrar los resultados
print("Conteo de vocales:")
for vocal, cantidad in resultado_vocales.items():
    print(f"{vocal.upper()}: {cantidad}")
