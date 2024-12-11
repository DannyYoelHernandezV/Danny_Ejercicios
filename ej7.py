class Pila:
    def __init__(self):
       
        self.elementos = []  # Lista que almacenará los elementos de la pila

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

def verificar_balanceado(cadena):
   
    pila = Pila()  # Crear una pila vacía
    #Diccionario para emparejar los paréntesis
    pares = {')': '(', '}': '{', ']': '['}
    
    for char in cadena:
        if char in '({[':  
            pila.push(char)  
        elif char in ')}]': 
            if pila.peek() == pares[char]:  
                pila.pop()  
            else:
                return False 
    return pila.peek() is None  


print(verificar_balanceado("()"))  
print(verificar_balanceado("{[()]}"))  
print(verificar_balanceado("[({})]"))  
print(verificar_balanceado("({[)]}"))  
print(verificar_balanceado("((()))"))  
print(verificar_balanceado("{[(])}"))  
