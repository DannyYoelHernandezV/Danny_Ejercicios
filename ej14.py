class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, elemento):
        self.elementos.append(elemento)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.elementos.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.elementos[0]

    def is_empty(self):
        return len(self.elementos) == 0

    def size(self):
        return len(self.elementos)

def reorganizar_cola(cola):
    cola_pares = Cola()
    cola_impares = Cola()

    while not cola.is_empty():
        numero = cola.dequeue()
        if numero % 2 == 0:
            cola_pares.enqueue(numero)
        else:
            cola_impares.enqueue(numero)

    while not cola_pares.is_empty():
        cola.enqueue(cola_pares.dequeue())

    while not cola_impares.is_empty():
        cola.enqueue(cola_impares.dequeue())


cola = Cola()
cola.enqueue(3)
cola.enqueue(100)
cola.enqueue(17)
cola.enqueue(18)
cola.enqueue(5)
cola.enqueue(60)

reorganizar_cola(cola)

while not cola.is_empty():
    print(cola.dequeue())
