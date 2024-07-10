# Programa 8 | for

print('+-------------------------------------+')
print("|Convertir grados Celsius a Fahrenheit|")
print('+-------------------------------------+ \n')


ce_in= int(input("Ingresa la temperaruta en °C inicial: "))
ce_fin = int(input("Ingresa la temperatuta en °C final: "))

print("\n")

print("Celsius     |      Fahrenheit")
print("_____________________________\n")

for temperatura in range(ce_in, ce_fin + 1): 
	f = (temperatura * (9 // 5)) + 32
	print(f'{temperatura} °C en fahrenheit es {f} °F')
