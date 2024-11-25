#Ejercicio 8
#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
#También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")
# Función que cuenta cuántos nombres comienzan con una letra específica
def contar_nombres_por_letra(nombres, letra):
    # Usamos una comprensión de lista para filtrar los nombres que empiezan con la letra indicada
    return sum(1 for nombre in nombres if nombre.lower().startswith(letra.lower()))

# Lista de nombres
nombres = ["Ana", "Luis", "Carlos", "Alejandro", "Pedro", "Andrea", "María", "Antonio", "Laura", "Adriana"]

# Pedir al usuario la letra a buscar
letra_buscada = input("Ingresa una letra para contar cuántos nombres empiezan con ella: ")

# Contamos cuántos nombres empiezan con la letra seleccionada
cantidad_nombres = contar_nombres_por_letra(nombres, letra_buscada)

# Imprimir el resultado
print(f"Hay {cantidad_nombres} nombres que comienzan con la letra '{letra_buscada.upper()}'.")
