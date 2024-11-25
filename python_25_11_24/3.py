#Ejercicio 3
#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
#  y devuelva las palabras que tengan mas de n caracteres.
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

# Función que recibe una lista de palabras y un número entero n,
# y devuelve las palabras que tengan más de n caracteres.
def filtrar_palabras(palabras, n):
    # Usamos una comprensión de lista para filtrar las palabras que tienen más de n caracteres.
    return [palabra for palabra in palabras if len(palabra) > n]


lista_palabras = ["manzana", "banana", "kiwi", "fresa", "sandía", "pera"]
n = 5
resultado = filtrar_palabras(lista_palabras, n)
print("Palabras con más de", n, "caracteres:", resultado)



