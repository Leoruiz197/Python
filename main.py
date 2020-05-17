import re
import funcoes
import time

emails = {}


print("/////////////////----------------////////////////////////---------------////////////////////")
print("\n")
print("Simple Dictionary email leak checker by Leonardo Ruiz Orabona - RM 85114")
print("\n")
print("/////////////////----------------////////////////////////---------------////////////////////")
print("\n")

time.sleep(1)

resp = "N"

while resp == "N":
    
    time.sleep(2)

    print("\nDigite uma opção do menu:\n")
    print("Digite 1 para Cadastrar vazamento")
    print("Digite 2 para Listar vazamento cadastrado")
    print("Digite 3 para Buscar por email")
    print("Digite 4 para Sair")
   
    opcao = int(input("\nQual opção escolhida? \n"))
    if opcao == 1:
        funcoes.cadastrar(emails)
    elif opcao == 2:
        funcoes.exibir(emails)
    elif opcao == 3:
        funcoes.buscar(emails)
    elif opcao == 4:
        resp = input("Deseja realmente sair? S/N\n").upper()
    else:
        print("Opção inválida!")
        print("Tente novamente!")