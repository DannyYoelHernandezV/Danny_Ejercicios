class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, elemento):    #Agrega un elemento al final de la cola
       
        self.elementos.append(elemento)

    def dequeue(self):      #Elimina y retorna el primer elemento de la cola
        
        if len(self.elementos) > 0:
            return self.elementos.pop(0) 
        return None  
    
    def peek(self):    #Devuelve el primer elemento de la cola sin eliminarlo
        
        if len(self.elementos) > 0:
            return self.elementos[0]
        return None  

cola = Cola()
cola.enqueue(1)  
cola.enqueue(2)
cola.enqueue(3)  

print("Elemento en el frente de la cola:", cola.peek())  
print("Elemento desencolado:", cola.dequeue())  

print("Elemento en el frente de la cola después de dequeue:", cola.peek())  
