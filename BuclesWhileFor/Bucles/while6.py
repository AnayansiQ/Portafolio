print('+-------------------------------+')
print("|Mostrar multitplos de un numero|")
print('+-------------------------------+ \n')

numero = int(input("Ingresa un numero: "))
inicio = 1

while numero > 0:
	resultado = numero * inicio
	print(numero , "*", inicio, "=", resultado)
	inicio += 1
	if inicio > 10:
	 break
	