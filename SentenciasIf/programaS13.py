
print('+-------------------------------+')
print("|Determina si un año es un siglo|")
print('+-------------------------------+ \n')

# Solicita al usuario ingresar un año
año = float(input("Ingrese un año: "))

print("\n")

# Comprueba si el año es divible entre 100
if año % 100 == 0: 
    print("Primer año de un siglo")

# Si no es divisible imprime un else    
else: 
    print("No es el primer año de un siglo")
