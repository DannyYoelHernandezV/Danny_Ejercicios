class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad  # Longitud máxima de la cola
        self.cola = [None] * capacidad  # Inicializamos la cola con valores None
        self.frente = 0  # Apunta al primer elemento
        self.ultimo = 0  # Apunta al siguiente espacio vacío
        self.tamano = 0  # Mantiene el número de elementos en la cola

    def enqueue(self, elemento):
        
        if self.is_full():
            print("La cola está llena. Se eliminará el primer elemento para agregar uno nuevo.")
            self.dequeue() 
        self.cola[self.ultimo] = elemento
        self.ultimo = (self.ultimo + 1) % self.capacidad 
        self.tamano += 1

    def dequeue(self):
       
        if self.is_empty():
            print("La cola está vacía.")
            return None
        elemento = self.cola[self.frente]
        self.cola[self.frente] = None  
        self.frente = (self.frente + 1) % self.capacidad  
        self.tamano -= 1
        return elemento

    def peek(self):
        
        if self.is_empty():
            print("La cola está vacía.")
            return None
        return self.cola[self.frente]

    def is_empty(self):
        
        return self.tamano == 0

    def is_full(self):
       
        return self.tamano == self.capacidad


cola = ColaCircular(3) 

cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print("Primer elemento:", cola.peek())  
cola.enqueue(4)  


print("Desencolando:", cola.dequeue())  # Debería ser 2
print("Desencolando:", cola.dequeue())  # Debería ser 3
print("Desencolando:", cola.dequeue())  # Debería ser 4
