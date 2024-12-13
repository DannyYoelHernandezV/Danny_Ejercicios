import heapq
from collections import Counter

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


def construir_arbol_huffman(mensaje):
    # Contar frecuencias
    frecuencias = Counter(mensaje)
    
    # Crear una cola de prioridad
    cola_prioridad = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in frecuencias.items()]
    heapq.heapify(cola_prioridad)
    
    while len(cola_prioridad) > 1:
        # Extraer los dos nodos con menor frecuencia
        izquierda = heapq.heappop(cola_prioridad)
        derecha = heapq.heappop(cola_prioridad)
        
        # Crear un nuevo nodo combinado
        combinado = NodoHuffman(None, izquierda.frecuencia + derecha.frecuencia)
        combinado.izquierda = izquierda
        combinado.derecha = derecha
        
        # Insertar el nodo combinado de nuevo en la cola
        heapq.heappush(cola_prioridad, combinado)
    
    # El último nodo en la cola es la raíz del árbol
    return cola_prioridad[0]


def crear_tabla_codigos(raiz, codigo_actual="", tabla_codigos=None):
    if tabla_codigos is None:
        tabla_codigos = {}
    if raiz:
        if raiz.caracter is not None:  # Es una hoja
            tabla_codigos[raiz.caracter] = codigo_actual
        crear_tabla_codigos(raiz.izquierda, codigo_actual + "0", tabla_codigos)
        crear_tabla_codigos(raiz.derecha, codigo_actual + "1", tabla_codigos)
    return tabla_codigos


def codificar_mensaje(mensaje, tabla_codigos):
    return ''.join(tabla_codigos[caracter] for caracter in mensaje)


def decodificar_mensaje(mensaje_codificado, raiz):
    mensaje_decodificado = []
    nodo_actual = raiz
    for bit in mensaje_codificado:
        nodo_actual = nodo_actual.izquierda if bit == "0" else nodo_actual.derecha
        if nodo_actual.caracter:  # Nodo hoja
            mensaje_decodificado.append(nodo_actual.caracter)
            nodo_actual = raiz
    return ''.join(mensaje_decodificado)


def mostrar_arbol_huffman(nodo, prefijo=""):
    if nodo is not None:
        if nodo.caracter:
            print(f"{prefijo} ─ '{nodo.caracter}' ({nodo.frecuencia})")
        else:
            print(f"{prefijo} ─ * ({nodo.frecuencia})")
        mostrar_arbol_huffman(nodo.izquierda, prefijo + "    ")
        mostrar_arbol_huffman(nodo.derecha, prefijo + "    ")


def main():
    # Paso 1: Leer mensaje de entrada
    mensaje = input("Introduce un mensaje: ")
    
    # Paso 2: Construir el árbol de Huffman
    raiz = construir_arbol_huffman(mensaje)
    
    # Mostrar el árbol si el mensaje es corto
    if len(mensaje) <= 10:
        print("\nÁrbol de Huffman:")
        mostrar_arbol_huffman(raiz)
    
    # Paso 3: Crear la tabla de códigos
    tabla_codigos = crear_tabla_codigos(raiz)
    print("\nTabla de Códigos:")
    for caracter, codigo in tabla_codigos.items():
        print(f"'{caracter}': {codigo}")
    
    # Paso 4: Codificar el mensaje
    mensaje_codificado = codificar_mensaje(mensaje, tabla_codigos)
    print(f"\nMensaje Codificado: {mensaje_codificado}")
    
    # Paso 5: Decodificar el mensaje
    mensaje_decodificado = decodificar_mensaje(mensaje_codificado, raiz)
    print(f"Mensaje Decodificado: {mensaje_decodificado}")
    
    # Paso 6: Mostrar estadísticas
    print(f"\nNúmero de bits en el mensaje codificado: {len(mensaje_codificado)}")
    print(f"Número de caracteres en el mensaje original: {len(mensaje)}")


if __name__ == "__main__":
    main()
