print('+-------------------+')
print("|Contador de digitos|")
print('+-------------------+ \n')

numero = int(input("Ingresa un numero: "))

digitos = 0
numero_x = numero

while numero_x != 0: 
	numero_x //= 10
	digitos += 1
print(f'El numero {numero} tiene {digitos} digito')