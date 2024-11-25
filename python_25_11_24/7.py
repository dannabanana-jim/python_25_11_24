#Ejercicio 7
#Definir una tupla con 10 edades de personas.
#Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

# Función para contar las edades mayores a 20
def contar_mayores_a_20(edades):
    # Usamos una comprensión de lista para contar las edades mayores a 20
    return sum(1 for edad in edades if edad > 20)

# Opción 1: Definir las edades directamente en una tupla
# edades = (18, 22, 34, 25, 19, 21, 17, 40, 30, 24)

# Opción 2: Pedir al usuario que ingrese las edades
edades = []
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    edades.append(edad)

# Convertir la lista a tupla
edades = tuple(edades)

# Contamos cuántas personas tienen edades mayores a 20
cantidad_mayores_a_20 = contar_mayores_a_20(edades)

# Imprimir el resultado
print(f"Hay {cantidad_mayores_a_20} personas con edades mayores a 20.")
