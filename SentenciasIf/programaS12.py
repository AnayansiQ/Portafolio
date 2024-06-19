
print('+--------------------------+')
print("| Calcular el salario neto |")
print('+--------------------------+ \n')

# Solicita al usuario ingresar su salario

salario = float(input("Ingrese su salario bruto: $ "))


# Verifica si el salario es mayor a $2000 
# Calcula el salario neto

if salario > 2000:
	impuesto = salario * 0.2
	salario_brut = salario - impuesto
	print(f"El salario bruto luego de aplicar el impuesto es ${salario_brut}")
	
# Si el salario es menor de $2000 no se aplican impuestos
else:
	salario_brut = salario
	print(f"El salario neto sin cobrar impuestos es ${salario_brut}")