# Programa 5 | for

print('+------------------------+')
print("|Imprimir numeros impares|")
print('+------------------------+ \n')

numero = int(input("Ingresa un numero: "))

print("\n")

if numero %  2 != 0: 
  for i in range(1, numero+1, 2):
  	print(f'{i}')
else: 
	print("El numero es par")
  	