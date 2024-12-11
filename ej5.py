def eliminar_duplicados(arreglo):
    
    unicos = []  
    for numero in arreglo:  
        if numero not in unicos:  
            unicos.append(numero) 
    return unicos


arreglo = [1, 3, 7, 7, 8]
arreglo_sinduplicados = eliminar_duplicados(arreglo)
print("Arreglo original:", arreglo)
print("Arreglo sin duplicados:", arreglo_sinduplicados)