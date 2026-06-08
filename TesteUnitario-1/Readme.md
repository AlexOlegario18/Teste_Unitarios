# Projeto de Testes Unitários em Python com IA

**Alexsander Davi Naves Olegário.**


**Engenharia de Software**

## Objetivo da Atividade

O principal objetivo desta atividade é explorar como ferramentas de IA podem ser utilizadas de forma **crítica e responsável** para:

*   **Gerar Cenários de Teste:** Identificar casos normais, de borda e de erro para funções de software.
*   **Validar Sugestões:** Analisar e refinar as propostas da IA, garantindo a correção das entradas e saídas esperadas.
*   **Implementar Testes:** Converter cenários validados em código de teste funcional usando o módulo `unittest` do Python.
*   **Ampliar Cobertura:** Adicionar novos testes a um projeto existente, como uma calculadora, para aumentar a robustez.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

*   **`calculadora.py`**: Contém as funções matemáticas básicas (`somar`, `subtrair`, `multiplicar`, `dividir`) e uma função para calcular a média de uma lista de números.
*   **`test_calculadora.py`**: Contém os testes unitários implementados para as funções em `calculadora.py`. Estes testes foram desenvolvidos com o auxílio de uma IA generativa para a identificação de cenários e geração de código.

## Uso da IA na Atividade

A IA foi empregada em duas etapas principais para o desenvolvimento dos testes:

1.  **Geração de Cenários de Teste:** Prompts específicos foram utilizados para solicitar à IA uma lista abrangente de cenários de teste para cada função em `calculadora.py`. Os cenários incluíram casos normais, de borda (ex: números zero, negativos, listas com um único elemento) e de erro (ex: divisão por zero, lista vazia para média).

    *Exemplo de prompt para `somar(a, b)`:*
    ```
    Atue como um professor de Teste de Software.
    Tenho a seguinte função Python:
    def somar(a, b):
        return a + b
    Quero criar testes unitários usando unittest.
    Antes de gerar o código, liste cenários de teste para essa função.
    Para cada cenário, informe:
    - nome do cenário;
    - entrada usada;
    - resultado esperado;
    - tipo do cenário: caso normal, caso de borda ou caso de erro.
    Use linguagem simples, pois sou iniciante em testes unitários.
    ```

2.  **Transformação de Cenários em Código:** Após a validação dos cenários, um segundo conjunto de prompts foi usado para gerar o código Python (`unittest`) correspondente. A IA foi instruída a fornecer apenas os métodos de teste para integração na classe `TestCalculadora`.

    *Exemplo de prompt para gerar código de teste:*
    ```
    Agora transforme os cenários anteriores em testes unitários usando Python e unittest.
    Considere que a função somar(a, b) está no arquivo calculadora.py.
    Gere apenas o método de teste que deve ser colocado dentro da classe TestCalculadora.
    ```

Esta metodologia permitiu otimizar o processo de criação de testes, mantendo o controle e a responsabilidade do desenvolvedor na validação e integração do código gerado pela IA.
