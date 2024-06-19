print('+-------------------------------------------+')
print("|Determina si un caracter es letra o digito.|")
print('+-------------------------------------------+ \n')

caracter = input("Ingresa un caracter: ")

print('\n')

if ('A' <= caracter <= 'Z') or ('a' <= caracter <= 'z'):
    print("Letra")
    
if '0' <= caracter <= '9': 
    print("Digito")