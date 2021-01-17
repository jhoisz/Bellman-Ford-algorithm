from aresta import Aresta
import time 
# função que executa o algoritmo de Bellman Ford
#recebe: lista de arestas, número de vértices e número de arestas
def bellmanFord(arestas, nVertices, nArestas):
    pai = list(range(nVertices)) # lista que armazena os vértices do caminho mais curto
    valor = list() # lista que armazena o valor da soma das arestas
    # distancia = list(range(nVertices)) # lista que armazena a distancia de um vertice para outro
    inf = float('inf') #variavel infinita
    #define o valor de cada vértice como infinito
    for i in range(0, nVertices):
        valor.append(inf)

    #inicializa o vértice 0 com o valor 0 e o seu pai como -1
    pai[0] = -1
    valor[0] = 0

    #variavel que verifica a necessidade de realizar a operação de relaxamento
    updated = bool

    #primeiro for que realiza v-1 relaxamentos até encontrar o caminho mais curto
    for i in range(1, nVertices-1):
        updated = False
        #for que percorre aresta por aresta e atribui o seu valor e seu vértice pai
        for j in range(0, nArestas):
            U = arestas[j].origem
            V = arestas[j].destino
            wt = arestas[j].peso
            #SE o valor do vértice U + o peso de sua aresta for menor que o valor antes atribuido ao vértice V faz-se o relaxamento
            if(valor[U]!=inf and valor[U]+wt<valor[V]):
                valor[V] = valor[U]+wt
                pai[V] = U
                # distancia[V] = valor[V]
                updated = True
        if updated==False:
            break

    #ultima verificação de relaxamento
    for j in range(0, nArestas):
        if(updated==True):
            U = arestas[j].origem
            V = arestas[j].destino
            wt = arestas[j].peso
            #se ainda houver possibilidade de realizar o relaxamento, então o grafo tem ciclo de peso negativo
            if(valor[U]!=inf and valor[U]+wt<valor[V]):
                print("Graph possui um ciclo de peso negativo. \n")
                return
    #wxibição dos caminhos encontrados
    for i in range(1, nVertices):
        print("Distância do vértice 0 para o vértice {} = {} (U->V: {}->{})".format(pai[i], valor[i], pai[i], i))

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



import time

inicio = time.time()
#execução do algoritmo de bellman Ford
bellmanFord(arestas, nVertices, nArestas)
fim = time.time()
print(fim - inicio)