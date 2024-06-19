print('+-----------------------------------------------+')
print("|Verificar si una palabra tiene mas de 5 letras.|")
print('+-----------------------------------------------+ \n')


Palabra = input("Ingresa una palabra: ")

print('\n')

cant_palabra = len(Palabra.strip())

if cant_palabra >= 5:
	print("La palabra tiene 5 letras") 
	
else:
	print("La palabra tiene menos de 5 letras")

      
	
