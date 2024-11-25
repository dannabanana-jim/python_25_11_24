#Ejercicio 1
#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte),
# solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son.
#  Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
# Función que recibe una lista de números y devuelve el más grande.
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")
def max_in_list(numeros):
    # La función max() ya está optimizada para encontrar el máximo en una lista.
    return max(numeros)


numeros = [1, 5, 3, 9, 2]
resultado = max_in_list(numeros)
print("El número más grande es:", resultado)
