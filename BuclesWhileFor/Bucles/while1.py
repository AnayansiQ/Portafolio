# Programa 1 | while

print('+--------------------------+')
print("|Sumar numeros del 1 al 100|")
print('+--------------------------+')

#Se crea una variable con un valor inicializado

contador = 0
suma = 0

while contador <= 100:
      suma += contador
      contador += 1
      print(f'Suma {suma}')
      print(f'Numero {contador}')

print(f'La suma de los numeros del 1 al 100 es {suma}')
  
        
