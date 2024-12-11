class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        print("Lista:", elementos)

def combinar_listas(lista1, lista2):
    nueva_lista = ListaEnlazada()
    actual1 = lista1.cabeza
    actual2 = lista2.cabeza

    while actual1 and actual2:
        if actual1.valor <= actual2.valor:
            nueva_lista.agregar(actual1.valor)
            actual1 = actual1.siguiente
        else:
            nueva_lista.agregar(actual2.valor)
            actual2 = actual2.siguiente

    while actual1:
        nueva_lista.agregar(actual1.valor)
        actual1 = actual1.siguiente

    while actual2:
        nueva_lista.agregar(actual2.valor)
        actual2 = actual2.siguiente

    return nueva_lista


lista1 = ListaEnlazada()
lista1.agregar(1)
lista1.agregar(3)
lista1.agregar(5)

lista2 = ListaEnlazada()
lista2.agregar(2)
lista2.agregar(4)
lista2.agregar(6)

lista1.mostrar()  
lista2.mostrar()  

lista_combinada = combinar_listas(lista1, lista2)
lista_combinada.mostrar()  
