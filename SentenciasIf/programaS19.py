print('+------------------------------------------------+')
print("|Verificar si un nombre es corto, mediano o largo|")
print('+------------------------------------------------+ \n')

Nombre = str(input("Ingresa tu nombre: "))

print('\n')

cant_letras = len(Nombre)

if cant_letras <= 5: 
    print("El nombre es corto")
    
elif cant_letras > 5 and cant_letras <= 8:  
    print("El nombre es mediano")
    
else: 
    print("El nombre el largo")
 

