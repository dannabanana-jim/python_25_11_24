#Ejercicio 2
#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

# Función que recibe una lista de palabras y devuelve la más larga.
def mas_larga(palabras):
    # Usamos la función max() con la clave len para encontrar la palabra más larga.
    return max(palabras, key=len)


lista_palabras = ["manzana", "banana", "kiwi", "fresa", "sandía"]
resultado = mas_larga(lista_palabras)
print("La palabra más larga es:", resultado)



