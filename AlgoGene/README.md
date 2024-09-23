# Algoritmo Genético para Minimização de f(x) = x³ - 6x + 14

Este projeto implementa um algoritmo genético em Python para encontrar o valor de `x` que minimiza a função `f(x) = x³ - 6x + 14`, com `x` sendo representado como um número real no intervalo [-10, +10].

## Descrição do Algoritmo

O algoritmo genético simula um processo evolutivo para encontrar o valor de `x` que resulta no menor valor de `f(x)`. Ele usa operações de seleção, crossover e mutação para "evoluir" uma população de indivíduos, onde cada indivíduo representa um valor possível de `x`.

### Funcionalidades

- **Codificação de `x` como um vetor binário**: O valor de `x` é representado em formato binário.
- **População inicial configurável**: Tamanho da população pode ser definido.
- **Crossover de 1 ou 2 pontos**: Pode escolher entre crossover de 1 ponto ou 2 pontos de corte.
- **Mutação**: Aplicada com uma taxa configurável (padrão 1%).
- **Seleção por torneio ou roleta viciada**: O algoritmo suporta ambas as opções de seleção.
- **Elitismo configurável**: Mantém uma porcentagem dos melhores indivíduos em cada geração.
- **Critério de parada**: Número máximo de gerações pode ser definido.

## Requisitos

Certifique-se de ter Python instalado. Não há dependências externas para esse código.

## Como Executar

1. Clone este repositório ou faça o download dos arquivos.

2. Execute o script `algoritmo_genetico.py`:
    ```bash
    python algoritmo_genetico.py
    ```

3. O algoritmo irá imprimir o melhor valor de `x` encontrado e o valor mínimo da função `f(x)`.

## Configurações

Você pode modificar as seguintes configurações no código:

- **Tamanho da população**: Altere o valor de `tamanho_populacao` (padrão: 10).
- **Número de gerações**: Defina o número máximo de gerações com `geracoes` (padrão: 100).
- **Taxa de mutação**: Configure a taxa de mutação com `taxa_mutacao` (padrão: 0.01).
- **Tipo de crossover**: Escolha entre "1ponto" ou "2pontos" na variável `tipo_crossover`.
- **Método de seleção**: Use "torneio" ou "roleta" na variável `tipo_selecao`.
- **Elitismo**: Ative/desative elitismo com `elitismo_ativo` (padrão: True) e defina o percentual de elitismo com `percentual_elitismo`.

### Exemplo de Saída

Melhor valor de x encontrado: -2.157
Valor mínimo da função f(x): 1.873






# Algoritmo Genético para o Problema da Mochila

Este projeto implementa um algoritmo genético em Python para maximizar o valor de itens selecionados em uma mochila, respeitando uma restrição de peso máximo.

## Descrição do Algoritmo

O algoritmo genético simula um processo evolutivo para encontrar a melhor combinação de itens que maximize o valor total sem exceder o peso máximo permitido. Ele usa operações de seleção, crossover e mutação para "evoluir" uma população de cromossomos, onde cada cromossomo representa uma seleção de itens.

### Funcionalidades

- **População inicial aleatória**: Uma população inicial de cromossomos é gerada aleatoriamente.
- **Crossover de 1 ponto**: O algoritmo utiliza crossover de 1 ponto para combinar cromossomos.
- **Mutação**: Aplicada com uma taxa configurável (padrão 10%).
- **Seleção por torneio**: A seleção dos pais é feita através do método de torneio.
- **Critério de parada**: O algoritmo para após um número máximo de gerações.
- **Elitismo**: O melhor indivíduo de cada geração é preservado para a próxima geração, garantindo que a melhor solução encontrada seja mantida.

## Requisitos

Certifique-se de ter Python instalado. O código não depende de bibliotecas externas, apenas a biblioteca `random` padrão do Python é utilizada.

## Como Executar

1. Clone este repositório ou faça o download dos arquivos.

2. Execute o script `algoritmo_genetico.py`:
    ```bash
    python algoritmo_genetico.py
    ```

3. O algoritmo irá imprimir os melhores indivíduos de cada geração e a melhor solução final.

## Configurações

Você pode modificar as seguintes configurações no código:

- **Número de cromossomos**: Altere o valor de `num_cromossomos` (padrão: 150).
- **Número de gerações**: Defina o número máximo de gerações com `geracoes` (padrão: 50).
- **Taxa de mutação**: Configure a taxa de mutação com `taxa_mutacao` (padrão: 0.1).
- **Peso máximo**: Defina o peso máximo permitido na mochila com `peso_maximo` (padrão: 100).

### Exemplo de Saída

Melhores indivíduos por geração:
Geração 1: Valor = 815, Cromossomo = [1, 1, 1, 0, 0, 1, 0, 1, 1, 0]
Geração 2: Valor = 830, Cromossomo = [1, 1, 1, 1, 1, 1, 1, 0, 1, 0]
...

Melhor solução final: Valor = 830, Cromossomo = [1, 1, 1, 1, 1, 1, 1, 0, 1, 0]
