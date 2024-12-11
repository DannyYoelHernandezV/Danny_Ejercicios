class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  

    def agregar(self, valor):
        """Agrega un nuevo nodo con el valor al final de la lista."""
        nuevo_nodo = Nodo(valor)
        if not self.cabeza: 
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:  
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, valor):
        """Elimina el primer nodo que contiene el valor especificado."""
        if not self.cabeza: 
            print("La lista está vacía.")
            return
        
        if self.cabeza.valor == valor:  
            self.cabeza = self.cabeza.siguiente
            return
        
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.valor != valor:
            actual = actual.siguiente
        
        if actual.siguiente:  
            actual.siguiente = actual.siguiente.siguiente
        else:
            print(f"El valor {valor} no está en la lista.")

    def buscar(self, valor):
        """Busca un nodo con el valor especificado. Devuelve True si se encuentra."""
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        """Muestra todos los elementos de la lista."""
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
lista.mostrar()  

lista.eliminar(2)
lista.mostrar()  

print(lista.buscar(3))  
print(lista.buscar(4))  
