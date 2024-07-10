# Programa 3 | while

print('+-----------------------------+')
print("|Sumar numeros hasta un limite|")
print('+-----------------------------+ \n')

numero = int(input("Ingresa un numero positivo: "))
suma = 0
limite = 200

while suma < limite: 
	if numero > 0:
		suma += numero
		numero += 1
		print(f'suma {suma}')
		print(f'numero {numero}')
print(f'La suma de los numeros es {suma}')
   
	

