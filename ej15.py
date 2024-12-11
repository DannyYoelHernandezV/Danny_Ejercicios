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

def ordenar_cola(cola):
    n = cola.size()
    for _ in range(n):
    
        min_val = float('inf')
        size = cola.size()

        for _ in range(size):
            num = cola.dequeue()
            if num < min_val:
                min_val = num
            cola.enqueue(num)

        cola.enqueue(min_val)


cola = Cola()
cola.enqueue(7)
cola.enqueue(2)
cola.enqueue(77)
cola.enqueue(12)

ordenar_cola(cola)

while not cola.is_empty():
    print(cola.dequeue())
