class Pila:
    def __init__(self):
       
        self.elementos = []  

    def push(self, elemento):
       
        self.elementos.append(elemento)

    def pop(self):
       
        if self.peek() is not None:  
            return self.elementos.pop()
        return None 
    
    def peek(self):
       
        if len(self.elementos) > 0:
            return self.elementos[-1]
        return None  

def invertir_cadena(cadena):
  
    pila = Pila()  
    
    for char in cadena:
        pila.push(char)
    
    
    cadena_invertida = ''
    while pila.peek() is not None:  
        cadena_invertida += pila.pop()  

    return cadena_invertida

cadena = "¡Hola! ¿Cómo estás?"
print("Cadena original:", cadena)
print("Cadena invertida:", invertir_cadena(cadena))
