# Algoritmo de Bellman Ford

## Para executar:
- Insira a quantidade de vértices;
- Insira a quantidade de arestas;
- Insira cada aresta no formato (origem, destino, valor)

## Exemplos de entrada e saída:
- Entrada:

<p> 5 10 </p>
<p> 0 1 6 </p>
<p> 0 2 7 </p>
<p> 1 2 8 </p>
<p> 1 3 -4 </p>
<p> 1 4 5 </p>
<p> 2 3 9 </p>
<p> 2 4 -3 </p>
<p> 3 4 7 </p>
<p> 3 0 2 </p>
<p> 4 1 -2 </p>

- saida:
<p> Distância do vértice 0 para o vértice 4 = 2 (U->V: 4->1) </p>
<p> Distância do vértice 0 para o vértice 0 = 7 (U->V: 0->2) </p>
<p> Distância do vértice 0 para o vértice 1 = -2 (U->V: 1->3) </p>
<p> Distância do vértice 0 para o vértice 2 = 4 (U->V: 2->4) </p>