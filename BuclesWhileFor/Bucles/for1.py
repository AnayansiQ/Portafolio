#Programa 1 | for

print('+--------------------+')
print("|Tabla de multiplicar|")
print('+--------------------+ \n')

tabla = int(input("Ingresa un numero: "))

print("\n")

for multiplicador in range(1,11): 
    resultado = tabla * multiplicador
    print(f'{tabla} * {multiplicador} = {resultado}')