num = int(input("digite um numero inteiro "))                 #solicita um numero ao usuario

for x in range(1,11):                                         #define um laço iniciando em 1 ate 11
    print(f"{x} * {num} = ", end='')                 #mostra na tela x * numero escolhido = resultado
    print(num*x)
