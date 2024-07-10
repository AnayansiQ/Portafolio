# Programa 2 | while

print('+---------------------------+')
print("|Contar hasta un numero dado|")
print('+---------------------------+ \n')

num = int(input("Ingresa un numero: "))


suma = 1

while num < 0: 
    print("No es un numero positivo")
    num = int(input("Ingresa un numero: "))
    print('\n')
    
while suma <= num:
    print(suma)
    suma += 1
  

	
		
