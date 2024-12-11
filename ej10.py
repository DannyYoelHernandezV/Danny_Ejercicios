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

class Navegador:
    def __init__(self):
        self.historial = Pila()
        self.pagina_actual = None

    def navegar(self, url):
        if self.pagina_actual is not None:
            self.historial.push(self.pagina_actual)
        self.pagina_actual = url
        print(f"Navegando a: {url}")

    def ir_atras(self):
        if self.historial.peek() is not None:
            self.pagina_actual = self.historial.pop()
            print(f"Volviendo a: {self.pagina_actual}")
        else:
            print("No hay más páginas en el historial para ir hacia atrás.")

    def obtener_pagina_actual(self):
        return self.pagina_actual


navegador = Navegador()
navegador.navegar("www.youtube.com")
navegador.navegar("www.chatgpt.com")
navegador.navegar("www.facebook.com")
navegador.ir_atras()  
navegador.ir_atras()  
navegador.ir_atras()  
