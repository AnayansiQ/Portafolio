print('+-------------------------------------------+')
print("|Determinar el tioo de licencia de conducir.|")
print('+-------------------------------------------+ \n')

Edad = float(input("Ingresa tu edad: "))

print('\n')

if Edad <= 17:
    print("Licencia de Menor")
    
elif Edad <= 65:
    print("Licencia de Adulto")
    
else: 
    print("Licencia de adulto mayor")