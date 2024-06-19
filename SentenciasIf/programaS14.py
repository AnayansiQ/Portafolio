# Verifica si un triangulo es valido

print('+----------------------------------+')
print("|Verifica si un triangulo es valido|")
print('+----------------------------------+ \n')
# Solicita al usuario ingresar las longitudes de los lados del triangulo

lado_1 = float(input("Ingresa la longitud del lado 1: "))
lado_2 = float(input("Ingresa la longitud del lado 2: "))
lado_3 = float(input("Ingresa la longitud del lado 3: "))

print("\n")
# Se realiza la operacion para realizar la sumatoria de los lados 1 y 2
longitud_xy = lado_1 + lado_2 

# Comprueba si la suma de los lados 1 y 2 es mayor al lado 3

if longitud_xy > lado_3: 
    print("La suma de los lados 1 y 2 es mayor que la longitud del lado 3")

#Comprueba si los lados 1 y 2 son iguales al lado 3
    
elif longitud_xy == lado_3:
    print("Las longitudes son iguales")
    
# Si no es ninguna de las anteriores se imprime que el lado 3 es mayor

else: 
    print("La longitud del tercer lado es mayor")