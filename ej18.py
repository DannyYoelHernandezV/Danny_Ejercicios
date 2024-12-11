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

    def eliminar_duplicados(self):
        valores_vistos = set()
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.valor in valores_vistos:
                anterior.siguiente = actual.siguiente
            else:
                valores_vistos.add(actual.valor)
                anterior = actual
            actual = actual.siguiente

    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        print("Lista:", elementos)


lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(2)
lista.agregar(4)
lista.agregar(3)
lista.mostrar() 

lista.eliminar_duplicados()
lista.mostrar()  
