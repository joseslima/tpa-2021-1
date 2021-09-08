# Trabalho de Programação

**Dividir e Conquistar & Programação Dinâmica & Algoritmos Gulosos**

**Autor:** José Guilherme Silva de Lima

**Data:** 08 de setembro de 2021

**Problema:** 10131	- Is Bigger Smarter?

## Sobre a Solução
Este diretório contém o código fonte gerado para solucionar o problema 10131
do *Online Judge*. 

Para resolver esse problema foi utilizada a estratégia de programação dinâmica, através da variavel global denonimada "cache"
que faz o papel de aarmazenar na memória o resultaado dos calculos realizados na função "walk". Essa variavel é utilizada para fazer 
a comparação reaalizada na função `getBigger`.


O problema recebeu veredito “Accepted”, como mostrado na
figura abaixo:

![Veredito](./10131-veredito.png)

O programa foi desenvolvido em Python3. Para compilar o programa deve ser usado
o seguinte comando:
```
python3 10131.py
```
caso deseje utilizar algum arquivo txt como input, execute o seguinte comando:
```
python3 10131.py < input.txt
```


