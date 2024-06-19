
print('+----------------------------+')
print("|Calcular la tarifa de un taxi|")
print('+----------------------------+ \n')

# Solicita al usuario ingresar la distancia
distancia = float(input("Ingresa la distancia recorrida en km: "))


# Definir la distancia inicial
dist_inicial = 10

 
# Calcular la tarifa si la distancia es menor o igual a 10 km

if distancia <= dist_inicial: 
    tarifa_inicial = 2.50
    tarifa_total = distancia * tarifa_inicial
    print(f'La tarifa total es $ {tarifa_total}')
     
# Calcular la tarifa si la distancia es mayor a la distancia inicial

else: 
    distancia > dist_inicial
    tarifa_inicial = 2.50
    tarifa_ad = 2.00
    tarifa_total2 = dist_inicial * tarifa_inicial +  (distancia - dist_inicial) * 2.00
    print(f'La tarifa adicional es ${tarifa_total2: .2f}')
    
   
    
    
    
    
    