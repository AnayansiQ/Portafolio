# Programa 5 | while

print('+--------------------------------------+')
print("|Sumar los primeros N numeros naturales|")
print('+--------------------------------------+ \n')

import random

resp_correcta = random.randint(1,10)

resp_incorrecta = 0

while resp_incorrecta != resp_correcta: 
	num = int(input("Adivina el numero entre 1 y 10: "))
	if num == resp_correcta: 
		print("¡Lo has encontrado!")
		break
	elif num > resp_correcta: 
		print("El numero es menor")
	elif num < resp_correcta:
		print("El numero es mayor")

print("Fin")
	
