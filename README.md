# Algoritmo de Bellman Ford

## Para executar:
- Insira a quantidade de vértices;
- Insira a quantidade de arestas;
- Insira cada aresta no formato (origem, destino, valor)

## Exemplos de entrada e saída:

<table>
    <thead>
        <th>Entrada</th>
    <thead>
    <tbody>
        <tr>5 10</tr>
        <tr> 0 1 6 </tr>
        <tr> 0 2 7 </tr>
        <tr> 1 2 8 </tr>
        <tr> 1 3 -4 </tr>
        <tr> 1 4 5 </tr>
        <tr> 2 3 9 </tr>
        <tr> 2 4 -3 </tr>
        <tr> 3 4 7 </tr>
        <tr> 3 0 2 </tr>
        <tr> 4 1 -2 </tr>
    </tbody>
</table>

<table>
    <thead>
        <th>Saída</th>
    <thead>
    <tbody>
        <tr> Distância do vértice 0 para o vértice 4 = 2 (U->V: 4->1) </tr>
        <tr> Distância do vértice 0 para o vértice 0 = 7 (U->V: 0->2) </tr>
        <tr> Distância do vértice 0 para o vértice 1 = -2 (U->V: 1->3) </tr>
        <tr> Distância do vértice 0 para o vértice 2 = 4 (U->V: 2->4) </tr>
    </tbody>
</table>