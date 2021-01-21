from aresta import Aresta
from bellmanFord import bellmanFord
import time 
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------------------#
#1° forma de atribuição de valores
# entrada de dados:
# arestas = list()
# nVertices = int(input("Digite o número de Vértices: "))
# nArestas = int(input("Digite o número de Arestas: "))

# print("Digite as {} arestas (origem, destino, peso): ".format(nArestas))
# for i in range(0, nArestas):
#     v1, v2, p = input().split(" ")
#     arestas.append(Aresta(int(v1), int(v2), int(p)))
#---------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------#
#2° forma de atribuição de valores
nVertices = 5 #definição do número de vertices do grafo
nArestas = 10 #definição do número de arestas do grafo
#definição das arestas em uma lista
arestas = [
    Aresta(0, 1, 6),
    Aresta(0, 2, 7),
    Aresta(1, 2, 8),
    Aresta(1, 3, -4),
    Aresta(1, 4, 5),
    Aresta(2, 3, 9),
    Aresta(2, 4, -3),
    Aresta(3, 4, 7),
    Aresta(3, 0, 2),
    Aresta(4, 1, -2)
]
#---------------------------------------------------------------------------------------#

inicio = time.time()
#execução do algoritmo de bellman Ford
bellmanFord(arestas, nVertices, nArestas)
fim = time.time()
print("Tempo de execução: {}".format(fim - inicio))
grafo1 = fim - inicio

nVertices = 7 #definição do número de vertices do grafo
nArestas = 9 #definição do número de arestas do grafo
arestas = [
    Aresta(0, 2, 7),
    Aresta(1, 0, 3),
    Aresta(1, 3, -3),
    Aresta(2, 5, -2),
    Aresta(4, 1, 6),
    Aresta(3, 4, -4),
    Aresta(4, 3, 6),
    Aresta(5, 4, 12),
    Aresta(4, 6, 7)
]

inicio = time.time()
#execução do algoritmo de bellman Ford
bellmanFord(arestas, nVertices, nArestas)
fim = time.time()
print("Tempo de execução: {}".format(fim - inicio))
grafo2 = fim - inicio

names = ['Grafo 1', 'Grafo 2']
values = [grafo1, grafo2]


x = [grafo1, grafo2]

plt.bar(range(len(x)), x, width=0.4, color='blue')
plt.show()