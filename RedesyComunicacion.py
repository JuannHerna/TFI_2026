"""
Redes y Comunicación
Crear un red de ocho nodos que muestre una relación 
direccionada, de manera que cada nodo sólo pueda tener 
comunicación directa con otros 2 nodos.   
"""

import networkx as nx
import matplotlib.pyplot as plt

"""
Redes y Comunicación
Crear una red de ocho nodos que muestre una relación 
direccionada, de manera que cada nodo solo pueda tener 
comunicación directa con otros 2 nodos.
Instale las dependencias 
pip install networkx matplotlib
python -m pip install networkx matplotlib
En el google colab se ve claramente el grafo.
"""


# 1. Crear el grafo dirigido
G = nx.DiGraph()

# 2. Definir los 8 nodos
nodos = [1, 2, 3, 4, 5, 6, 7, 8]
G.add_nodes_from(nodos)

# 3. Crear las conexiones: cada nodo apunta al siguiente y al que sigue de ese
n = len(nodos)
for i in range(n):
    actual = nodos[i]
    siguiente = nodos[(i + 1) % n]   # vecino inmediato
    siguiente2 = nodos[(i + 2) % n]  # segundo vecino
    G.add_edge(actual, siguiente)
    G.add_edge(actual, siguiente2)

# 4. Verificar que cada nodo tenga exactamente 2 conexiones salientes
print("Cantidad de nodos:", G.number_of_nodes())
print("Cantidad de conexiones (edges):", G.number_of_edges())
print("Grado de salida de cada nodo:", dict(G.out_degree()))

# 5. Dibujar el grafo
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=800, font_weight='bold', arrowsize=20)
plt.title("Red dirigida de 8 nodos (cada nodo con 2 conexiones)")
plt.show()

