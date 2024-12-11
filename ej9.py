class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if len(self.elementos) > 0:
            return self.elementos.pop()
        return None

    def peek(self):
        if len(self.elementos) > 0:
            return self.elementos[-1]
        return None

def calcular_rpn(expresion):
    pila = Pila()
    operadores = {'+', '-', '*', '/'}
    
    for item in expresion:
        if item not in operadores:
            pila.push(int(item))
        else:
            operando2 = pila.pop()
            operando1 = pila.pop()
            
            if item == '+':
                resultado = operando1 + operando2
            elif item == '-':
                resultado = operando1 - operando2
            elif item == '*':
                resultado = operando1 * operando2
            elif item == '/':
                if operando2 == 0:
                    return "Error: División por cero"
                resultado = operando1 / operando2
            
            pila.push(resultado)
    
    return pila.pop()

expresion = ["3", "4", "+", "2", "*", "7", "/"]
resultado = calcular_rpn(expresion)
print("Resultado de la expresión:", resultado)
