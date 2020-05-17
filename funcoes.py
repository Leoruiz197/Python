import re

def cadastrar(vazamento):
    check = "S"
    resp = "S"
    while resp == "S":
        tag = input("Qual o id do vazamento?")
        while check == "S": 
            email = input("Email vazado: ").upper()  
            if re.match("[^@]+@[^@]+\.[^@]+", email):
                check = "N"
            else:
                print("erro de entrada, email invalido")
                check = "S" 
        vazamento[tag] = [
            email,
            input("Senha do email: \n"),
            ]
        resp = input("\nDeseja cadastrar mais um email? S/N \n").upper()

def exibir(vazamento):
    for tag, lista in vazamento.items():
            print("\nTag.....", tag)
            print("Email.....", lista[0])
            print("Senha.....", lista[1])

def buscar(vazamento):
    busca = input("qual a tag do email?")
    lista = vazamento.get(busca)
    if lista != None:
        print("\nEmail.....", lista[0])
        print("Senha.....", lista[1])
    else:
        print("Vazamento não encontrado!")