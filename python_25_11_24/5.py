#Ejercicio 5
#Construir un pequeño programa que convierta números binarios en enteros.
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

# Programa que convierte un número binario en un entero.
def binario_a_entero(binario):
    # Usamos la función int() para convertir el número binario (en forma de cadena) a entero.
    return int(binario, 2)

# Solicitar al usuario que ingrese un número binario.
numero_binario = input("Ingresa un número binario: ")

# Convertimos el número binario a entero.
numero_entero = binario_a_entero(numero_binario)

# Mostramos el resultado.
print(f"El número binario {numero_binario} en entero es: {numero_entero}")

