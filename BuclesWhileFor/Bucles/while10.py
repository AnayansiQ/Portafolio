print('+----------------------------+')
print("|Simular un cajero automatico|")
print('+----------------------------+ \n')


PIN = 2213
intento = 0
limite = 3


while intento < limite:
	Numero = int(input("Ingresa el numero pin: "))
	if Numero == PIN: 
		print("Contraseña ingresada con exito")
		break
	elif Numero != PIN:
		intento += 1
		print("PIN incorrecto")
if intento == limite:
	print("su tarejat ha sido bloqueada")	
	

		
	