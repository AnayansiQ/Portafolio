# Programa 7 | for

print('+--------------------------------+')
print("|Determinar si un numero es primo|")
print('+--------------------------------+ \n')

numero = int(input("Ingresa un numero entero: "))
primo = True 

print("\n")

for i in range(2, numero, 2):
	if numero % i == 0: 
		print(f'{numero} No es primo')
		primo = False
		break
		
if primo: 
	print(f'{numero} Es primo')
	
			