def suma_elementos(arreglo):
    
    suma = 0  # Inicializamos la suma en 0
    for num in arreglo:  # Iteramos sobre cada número en el arreglo
        suma += num # Sumamos cada número al acumulador
    return suma


arreglo = [4, 1, 37, 45, 5]
resultado = suma_elementos(arreglo)
print("La suma de los elementos es:", resultado)