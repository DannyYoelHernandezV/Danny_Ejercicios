def invertir_arreglo(arreglo):
   
    arreglo_invertido = []  
    for i in range(len(arreglo) - 1, -1, -1):  # Iteramos desde el último índice al primero
        arreglo_invertido.append(arreglo[i])  # Añadimos cada elemento al nuevo arreglo
    return arreglo_invertido

arreglo = [4, 1, 37, 45, 5]
arreglo_invertido = invertir_arreglo(arreglo)
print("Arreglo original:", arreglo)
print("Arreglo invertido:", arreglo_invertido)