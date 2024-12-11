

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def inorder(self):
        elementos = []
        self._inorder_recursivo(self.raiz, elementos)
        return elementos

    def _inorder_recursivo(self, nodo, elementos):
        if nodo:
            self._inorder_recursivo(nodo.izquierdo, elementos)
            elementos.append(nodo.valor)
            self._inorder_recursivo(nodo.derecho, elementos)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        return self._buscar_recursivo(nodo.derecho, valor)


arbol = ArbolBinario()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)

print(arbol.inorder())  
print(arbol.buscar(10)) 
print(arbol.buscar(7))   