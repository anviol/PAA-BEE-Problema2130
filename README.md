# PAA-BEE-Problema2130

## Final Mundial de 2008
#### Por XI Maratona de Programação IME-USP, 2007 BR Brazil
#### Timelimit: 1

Preocupado com a atual situação de crise no transporte aéreo, o diretor regional do concurso do ICPC no Brasil já iniciou seus preparativos para fazer as reservas das passagens aéreas para as ﬁnais mundiais de Banff em 2008. O primeiro passo foi estudar a malha aérea disponível, em que cada voo tem um certo preço e liga duas cidades (estamos, na verdade, chamando de voo apenas um trecho non stop de um voo comercial). O objetivo do diretor é fazer várias consultas nesta malha de voos.

Em geral desejamos fazer voos sem escalas, mas estes podem ser muito caros. Para contornar este fato o diretor deseja permitir algumas escalas possíveis. Assim, ele ordenou as várias cidades da malha em sua ordem de preferência para fazer escala. Ou seja, a cidade de índice 1 é a que ele prefere fazer escala, seguida pela cidade 2, e assim por diante.

As consultas que o diretor fará são do seguinte tipo. É dada a cidade de partida e de chegada e um número t de cidades em que o diretor permite que sejam feitas escalas. Seu programa deverá encontrar o custo de um voo de custo mínimo entre as cidades que faça, no máximo, escalas nestas cidades. Por exemplo, se t = 1 você deverá encontrar o custo de um voo de custo mínimo entre as duas cidades que seja, ou non stop ou que faça uma escala na primeira cidade.

### Entrefa
A entrada é composta de diversas instâncias. A primeira linha de cada instância consiste em dois inteiros n (1 ≤ n ≤ 100) e m (1 ≤ m ≤ 100000), indicando o número de cidades e o número de escalas. Nas m linhas seguintes temos três inteiros u, v e w (1 ≤ u, v ≤ n e 0 ≤ w ≤ 100) indicando que existe uma escala que vai de u para v com custo w. Em seguida um inteiro c (1 ≤ c ≤ 10000) indicando o número de consultas e nas c linhas seguintes temos três inteiros o, d e t (1 ≤ o, d ≤ n e 1 ≤ t ≤ n) onde o é a cidade de origem, d é a cidade de destino e t indica que as cidades 1,2,..,t podem ser usadas para escalas.

A entrada termina com ﬁnal de arquivo.

### Saída
Para cada instância, você deverá imprimir um identificador Instância k, onde k é o número da instância atual. Para cada consulta, na ordem da entrada, você deve imprimir o custo mínimo ou -1 caso não exista caminho entre as duas cidades.

Após cada instância imprima uma linha em branco.

### Exemplo de Entrada

```bash
4 7
4 1 0
2 1 3
1 4 20
2 3 15
4 2 1
3 1 21
1 2 0
3
2 1 0
4 2 2
4 3 1
5 10
4 5 2
2 1 4
1 2 7
2 4 7
5 2 1
4 1 2
4 5 12
5 4 4
5 3 7
3 5 9
4
2 5 0
3 4 5
4 5 1
2 3 2
```

### Exemplo de Saída
```bash
Instancia 1
3
0
-1

Instancia 2
-1
13
2
-1
```
