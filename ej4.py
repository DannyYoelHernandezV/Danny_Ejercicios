def buscar_numero(arreglo, numero):
  
    for elemento in arreglo:  # Recorremos cada elemento del arreglo
        if elemento == numero:  # Comparamos con el número buscado
            return True
    return False

arreglo = [4, 1, 37, 45, 5]
numero_buscado = int(input("Ingresa un número para buscar: "))

if buscar_numero(arreglo, numero_buscado):
    print(f"El número {numero_buscado} está presente en el arreglo.")
else:
    print(f"El número {numero_buscado} NO está presente en el arreglo.")