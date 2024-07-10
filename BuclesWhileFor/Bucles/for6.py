# programa 6 | for

print('+--------------------------------------+')
print("|Sumar los primeros N numeros naturales|")
print('+--------------------------------------+ \n')

numero = int(input("Ingresa un numero: "))

print("\n")

suma = 0

for i in range(1, numero):
	print(i)
	suma += i
	
print("La suma de estos numeros es: ", suma)