print("+----------------------------------------+")
print("|Determina la categoria de un trabajador.|")
print("+----------------------------------------+ \n")

print("Comprobemos tu categoria según tus años de experiencia.")

print('\n')

# Solicita al usuario ingresar los años de experiencia
exp_años = float(input("Ingresa tus años de experiencia: "))

print("\n")

# Calcula la categoria si los años ingresados son mayores que 2


if 1 <= exp_años < 2: 
    print("Eres un Junior")
    
    
# Calcula si la experiencia es mayor de 2 años y menor que 5
    
elif 2 <= exp_años <= 5:
	print("Eres un Semi-senior")
	
# Calcula si la experiencia es mayor de 5 años

elif exp_años > 5: 
    print("Eres un Senior")
    
# Comprueba si el usuario no tiene ningun año de experiencia
else:
	exp_años == 0    
	print("No tienes experiencia")