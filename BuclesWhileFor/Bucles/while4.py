# Programa 4 | while

print('+--------------------------+')
print("|Sumar digitos de un numero|")
print('+--------------------------+ \n')


num = int(input("Ingresa un numero: "))

suma = 0
act_num = num

while act_num > 0:	
	digito = act_num % 10
	suma += digito
	act_num //= 10
	
print(f'La suma de los digitos de {num} es {suma}')
	