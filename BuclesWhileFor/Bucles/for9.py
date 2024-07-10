# Programa 9 | for

print('+----------------------------------+')
print("|Dibujar un triangulo de asteriscos|")
print('+----------------------------------+ \n')


numero = int(input("Ingresa un numero positivo: "))

print("\n")

for i in range(1, numero + 1):
	print("    *    " * i)
	print()
	
if numero < 0: 
	print("Intenta con un numero positivo")