# Análise de Algoritmos de Ordenação

Situação-problema: Central de Distribuição de Pedidos

## Objetivo

Desenvolver um experimento computacional em Python para comparar a quantidade de operações (comparações e trocas/movimentações) realizadas por quatro algoritmos de ordenação, avaliando qual apresenta melhor comportamento conforme o volume de dados aumenta.

## Algoritmos comparados

- Bubble Sort
- Insertion Sort
- Selection Sort
- Quick Sort

## Estrutura da atividade

- **Etapa 1 — Geração dos dados:** vetores de 10, 20 e 1.000 elementos, com cópias idênticas para cada algoritmo.
- **Etapa 2 — Contagem das operações:** cada algoritmo conta comparações e trocas/movimentações (critério de contagem documentado no relatório).
- **Etapa 3 — Resultados:** tabela com o total de operações de cada algoritmo, para cada tamanho de vetor.
- **Etapa 4 — Análise dos resultados:** respostas às questões a–i sobre o comportamento observado.
- **Desafio adicional:** repetição do experimento com vetor aleatório, já ordenado e em ordem inversa, analisando o impacto da organização inicial dos dados em cada algoritmo.

## Arquivos

| Arquivo | Descrição |
|---|---|
| `codigo_fonte(01-09).py` | Código em um único arquivo `.py` |
| `Pesquisa_e_Analise(01-09).pdf` | Relatório com critério de contagem, tabelas de resultados e respostas das questões |

## Principais resultados

- Com 1.000 elementos, Quick Sort realizou cerca de **40x menos comparações** que Bubble e Selection Sort.
- Bubble, Insertion e Selection Sort são todos O(n²), mas o Insertion Sort fez menos da metade das comparações dos outros dois, por interromper a busca assim que encontra a posição correta.
- No desafio adicional, o Quick Sort (com pivô fixo no último elemento) caiu no seu pior caso justamente no vetor já ordenado, igualando-se em comparações aos algoritmos O(n²), evidenciando que a organização dos dados de entrada afeta cada algoritmo de forma diferente.

Detalhes completos, tabelas e justificativas de todas as respostas estão no relatório (`.docx`).
