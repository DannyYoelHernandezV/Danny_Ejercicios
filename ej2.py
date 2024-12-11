def encontrar_max_min(arreglo):
   
    maximo = arreglo[0]
    minimo = arreglo[0]
    
    
    for numero in arreglo:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    
    return maximo, minimo

arreglo = [4, 1, 37, 45, 5]

maximo, minimo = encontrar_max_min(arreglo)
print("El valor máximo es:", maximo)
print("El valor mínimo es:", minimo)