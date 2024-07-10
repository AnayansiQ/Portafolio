# Programa 3 | for

print('+----------------------------+')
print("|Contar vocales en una cadena|")
print('+----------------------------+ \n')

palabra = input("Ingresa un texto: ")

print("\n")

vocales = "AEIOUaeiou"

contador = 0

for char in palabra: 
	if char in vocales: 
		contador += 1
		
print(f'{palabra} Tiene {contador} vocales')


