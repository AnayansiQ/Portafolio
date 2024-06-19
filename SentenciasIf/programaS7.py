# Calcula el precio con descuento
print('+------------------------------------+')
print("|Calcula el descuento de un producto.|")
print('+------------------------------------+ \n')

precio = float(input("Ingrese el precio del producto: "))

if precio > 100: 
    descuento = precio * 0.1
    p_final = precio - descuento
    print(f"El precio del producto es ${p_final: .2f} \n Se ha realizado un descuento del producto")
    
else: 
    p_final = precio
    print(f'${p_final}')
    print(f'No se aplica descuento')
 
 