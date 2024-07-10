# Programa 9 | while

numero = int(input("Ingresa un numero positivo: "))

while numero <= 0: 
	print("El numero ingresado no es positivo")
	numero = int(input("Ingresa un numero positivo: "))
	
print("\n")
	
bit = " "
residuo = numero

if residuo == 0:
	bit = "0"
	
while residuo > 0: 
	x = residuo % 2
	bit = str(x) + bit
	residuo = residuo // 2

print(f'El # binario de {numero} es {bit}')

