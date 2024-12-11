class Pila:
    def __init__(self):
       
        self.elementos = []  #Lista que almacenará los elementos de la pila

    def push(self, elemento):
        
        self.elementos.append(elemento)  # Agrega el elemento al final de la lista

    def pop(self):
        
        if not self.is_empty():  
            return self.elementos.pop()  
        return None  

    def peek(self):
        
        if not self.is_empty():
            return self.elementos[-1]  #Devuelve el último elemento sin eliminarlo
        return None  

    def is_empty(self):
        
        return len(self.elementos) == 0  #Si la lista está vacía, la pila también lo está


pila = Pila()

#Agregamos elementos a la pila
pila.push(10)
pila.push(20)
pila.push(30)


print("Elemento superior de la pila:", pila.peek())  

print("Elemento eliminado:", pila.pop())  

print("Elemento superior de la pila:", pila.peek())  


print("¿Está vacía la pila?", pila.is_empty())  


print("Elemento eliminado:", pila.pop()) 
print("Elemento eliminado:", pila.pop())  


print("¿Está vacía la pila?", pila.is_empty()) 
