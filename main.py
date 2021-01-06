from edge import Edge

def bellmanFord(Edges, V, E):
    parent = list(range(V))
    costParent = list(range(V))
    value = list(range(V, infinity))

    parent.append(-1)
    value.append(0)

    updated = False

    for i in range(0, V-1):
        updated = False

        for j in range(0, E):
            U = Edges[j].origem
            V = Edges[j].destino
            wt = Edges[j].peso

            if(value[U]!=infinity and value[U]+wt<value[V]):
                value[V] = value[U]+wt
                parent[V] = U
                costParent[V] = value[V]
                updated = True

        if updated==False:
            break
    for j in range(0, E):
        if(updated==True):
            U = Edges[j].origem
            V = Edges[j].destino
            wt = Edges[j].peso

            if(value[U]!=infinity and value[U]+wt<value[V]):
                print("Graph has -VE edge cycle\n")
                return
    for i in range(1, V):
        print("U->V: {} ->{}  Cost to reach {} from source 0 = {} \n".format(parent[i], i, parent[i], value[i]))
    

V = 5
E = 10
infinity = 999999 #ia usar o math.inf aqui mas ele n aceita, lê como float aí dá erro entao vo deixar assim por enquanto
Edges = [
    Edge(0, 1, 6),
    Edge(0, 2, 7),
    Edge(1, 2, 8),
    Edge(1, 3, -4),
    Edge(1, 4, 5),
    Edge(2, 3, 9),
    Edge(2, 4, -3),
    Edge(3, 4, 7),
    Edge(3, 0, 2),
    Edge(4, 1, -2)
]

bellmanFord(Edges, V, E)

# Exemplo:

# entrada:
# 5 10
# 0 1 6
# 0 2 7
# 1 2 8
# 1 3 -4
# 1 4 5
# 2 3 9
# 2 4 -3
# 3 4 7
# 3 0 2
# 4 1 -2

# saida:
# U->V: 4->1  Cost to reach 4from source 0 = 2
# U->V: 0->2  Cost to reach 0from source 0 = 7
# U->V: 1->3  Cost to reach 1from source 0 = -2
# U->V: 2->4  Cost to reach 2from source 0 = 4