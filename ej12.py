class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, elemento):
        
        self.elementos.append(elemento)

    def dequeue(self):
        
        if self.elementos:
            return self.elementos.pop(0)
        return "No hay más clientes en la cola"

    def peek(self):
        
        if self.elementos:
            return self.elementos[0]
        return "La cola está vacía"

cola = Cola()


cola.enqueue("Cliente 403")
cola.enqueue("Cliente 404")
cola.enqueue("Cliente 405")


print("Atendiendo:", cola.dequeue())  
print("Atendiendo:", cola.dequeue())  
print("Atendiendo:", cola.dequeue())  

print("Atendiendo:", cola.dequeue())  
