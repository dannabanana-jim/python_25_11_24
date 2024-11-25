#Ejercicio 10
#Escriba una función es_bisiesto() que determine si un año determinado es un año
#bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400

print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

def es_bisiesto(anio):
    """
    Determina si un año es bisiesto.

    Args:
        anio (int): El año a verificar.

    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    # Un año es bisiesto si es divisible por 4 pero no por 100, excepto si es divisible por 400
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False

# Ejemplo de uso
anio = int(input("Introduce un año: "))
if es_bisiesto(anio):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")
