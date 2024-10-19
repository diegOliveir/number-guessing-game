# Jogo de Adivinhação de Números

Este é um simples jogo de adivinhação de números em Python. O jogador define um intervalo entre dois números inteiros, e o sistema gera um número aleatório dentro desse intervalo. O jogador tem uma quantidade limitada de tentativas para adivinhar o número corretamente.

## Como funciona

1. O usuário define o limite inferior e o limite superior de um intervalo.
2. O sistema gera um número aleatório dentro do intervalo definido (incluindo os limites).
3. O número de tentativas permitidas é calculado com base no intervalo, utilizando a fórmula `log2(upper_bound - lower_bound + 1)`, arredondada para o número inteiro mais próximo.
4. O jogador faz tentativas de adivinhar o número. Após cada tentativa, o sistema indica se o palpite foi alto demais ou baixo demais.
5. O jogo termina quando o jogador adivinha o número corretamente ou quando as tentativas se esgotam.

## Requisitos

- **Python 3.x** deve estar instalado no seu sistema.
- Não é necessário instalar bibliotecas externas, apenas as bibliotecas padrão do Python (`random` e `math`).

## Como jogar

1. Execute o script Python.
2. Digite os valores para o limite inferior e superior do intervalo.
3. Tente adivinhar o número gerado pelo sistema.
4. O jogo irá fornecer feedback após cada tentativa, indicando se o seu palpite foi muito alto ou muito baixo.
5. O jogo termina quando você acertar o número ou quando acabar o número de tentativas.

### Exemplo de execução

```bash
Bem vindo ao jogo de adivinhação de números! 
Primeiramente você irá selecionar um intervalo entre dois números inteiros e o sistema irá gerar um número aleatório que fique entre os dois (incluindo os mesmos). Você terá uma quantidade limitada de tentativas para acertar. 
Boa sorte!

Digite o menor número inteiro do intervalo: 1
Digite o maior número inteiro do intervalo: 100
Você tem 6 chances!
Dê o seu palpite: 50
Você chutou alto demais! Lhe restam 5 tentativas.
Dê o seu palpite: 25
Você chutou baixo demais! Lhe restam 4 tentativas.
...
Parabéns! Você acertou com 4 tentativa/s!
```
## Regras

- O limite inferior deve ser menor que o limite superior.
- O número de chances é calculado automaticamente com base no intervalo, garantindo que você tenha uma quantidade justa de tentativas.

## Tratamento de Erros

- Caso o usuário digite algo que não seja um número inteiro, o sistema exibirá uma mensagem de erro e solicitará uma nova entrada.
- O jogo verifica se o limite inferior é realmente menor que o limite superior antes de prosseguir.

## Fonte de inspiração

Este projeto foi inspirado por um artigo do GeeksforGeeks sobre o jogo de adivinhação de números. Você pode conferir o artigo completo [aqui.](https://www.geeksforgeeks.org/number-guessing-game-in-python/)

## Contribuições

Sinta-se à vontade para fazer um fork deste projeto e sugerir melhorias!
