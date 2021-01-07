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
        <td>5 10</td>
        <td> 0 1 6 </td>
        <td> 0 2 7 </td>
        <td> 1 2 8 </td>
        <td> 1 3 -4 </td>
        <td> 1 4 5 </td>
        <td> 2 3 9 </td>
        <td> 2 4 -3 </td>
        <td> 3 4 7 </td>
        <td> 3 0 2 </td>
        <td> 4 1 -2 </td>
    </tbody>
</table>

<table>
    <thead>
        <th>Saída</th>
    <thead>
    <tbody>
        <td> Distância do vértice 0 para o vértice 4 = 2 (U->V: 4->1) </td>
        <td> Distância do vértice 0 para o vértice 0 = 7 (U->V: 0->2) </td>
        <td> Distância do vértice 0 para o vértice 1 = -2 (U->V: 1->3) </td>
        <td> Distância do vértice 0 para o vértice 2 = 4 (U->V: 2->4) </td>
    </tbody>
</table>