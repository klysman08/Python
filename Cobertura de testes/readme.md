# Exercício sobre Cobertura de Testes

Exercício formulado originalmente pelo Prof. Andre Hora.

Objetivo: entender e praticar conceitos básicos de cobertura de testes.

Nesse exercício, iremos utilizar o [Coverage.py](https://coverage.readthedocs.io/), principal ferramenta de cobertura de testes para Python.
Também iremos usar o [unittest](https://docs.python.org/3/library/unittest.html), principal framework de teste para Python.

## 1. Explore a classe Stack e seu teste

Primeiro, estude o código da classe `Stack` em `stack.py`, que implementa uma pilha.

Estude também o código da classe `TestStack` em `test_stack.py`. Veja que ela possui quatro métodos de teste.

## 2. Rode os testes de unidade 

Rode o unittest (framework de teste para Python), via linha de comando. Para isso, clique na aba **Shell** e digite:

 `python -m unittest`.

Observação: rode o comando acima no Shell e não no Console.

## 3. Instale o Coverage.py

Também no Shell, digite:

 `pip install coverage` 
 
 Ele vai instalar o Coverage.py, que é uma ferramenta que calcula a cobertura dos testes de um programa Python.


## 4. Rode os teste via Coverage.py

Agora, para rodar os testes de unidade, devemos utilizar o seguinte comando: 

`coverage run -m unittest`.

Rode o comando no Shell e veja o seu resultado. Ele deve informar que todos os testes foram executados com sucesso.


## 5. Gere o relatório de cobertura

Como os testes foram executados via `coverage`, você pode pedir para gerar o relatório de cobertura: 

`coverage report`.


Observe que a cobertura de `stack.py` é de 93%.

Para descobrir a linha que não está coberta por testes você pode usar:

`coverage report -m`.

O número da linha "descoberta" vai aparecer na coluna Missing.

## Exercício: Obtendo 100% de cobertura

Implemente um novo teste em `test_stack.py` que faça com que a cobertura aumente para 100%.

