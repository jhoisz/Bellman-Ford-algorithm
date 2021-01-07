# Algoritmo de Bellman Ford

## Para executar:
- Insira a quantidade de vértices;
- Insira a quantidade de arestas;
- Insira cada aresta no formato (origem, destino, valor).

## Exemplos de entrada e saída:


### Entrada

| vertices | arestas |
|:----------:|:---------:|
|     5    |    10   |  


| origem | destino | peso |
|:------:|:-------:|:----:|
|    0   |    1    |   6  |
|    0   |    2    |   7  |
|    1   |    2    |   8  |
|    1   |    3    |  -4  |
|    1   |    4    |   5  |
|    2   |    3    |   9  |
|    2   |    4    |  -3  |
|    3   |    4    |   7  |
|    3   |    0    |   2  |
|    4   |    1    |  -2  |


### Saída

| Resultado:                                                |
|-----------------------------------------------------------|
| Distância do vértice 0 para o vértice 4 = 2 (U->V: 4->1)  |
| Distância do vértice 0 para o vértice 0 = 7 (U->V: 0->2)  |
| Distância do vértice 0 para o vértice 1 = -2 (U->V: 1->3) |
| Distância do vértice 0 para o vértice 2 = 4 (U->V: 2->4)  |