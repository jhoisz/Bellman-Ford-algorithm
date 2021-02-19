from aresta import Aresta
from bellmanFord import bellmanFord
import time 

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
# 2° forma de atribuição de valores
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
bellmanFord(arestas, nVertices, nArestas, )
fim = time.time()
print("Tempo de execução: {}".format(fim - inicio))