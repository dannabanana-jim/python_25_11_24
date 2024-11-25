#Ejercicio 6
#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

# Función que calcula la edad de una persona según el año de nacimiento y el año actual.
def calcular_edad(anio_nacimiento, anio_actual):
    return anio_actual - anio_nacimiento

# Solicitar el año en curso (actual).
anio_actual = int(input("Ingresa el año en curso: "))

# Lista para almacenar la información de las personas.
personas = []

# Solicitar el nombre y año de nacimiento de tres personas.
for i in range(3):
    nombre = input(f"Ingresa el nombre de la persona {i+1}: ")
    anio_nacimiento = int(input(f"Ingresa el año de nacimiento de {nombre}: "))
    
    # Calcular la edad y almacenar la información.
    edad = calcular_edad(anio_nacimiento, anio_actual)
    personas.append((nombre, edad))

# Imprimir los resultados.
print("\nEdad de las personas que cumplirán en el año en curso:")
for nombre, edad in personas:
    print(f"{nombre} cumplirá {edad} años.")


