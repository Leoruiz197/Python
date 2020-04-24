import re

emails = []
check = "S"
emailValido = False
emailAlvo = ""
email = ""

print("/////////////////----------------////////////////////////---------------////////////////////")
print("\n")
print("Simple email leak checker by Leonardo Ruiz Orabona - RM 85114")
print("\n")
print("/////////////////----------------////////////////////////---------------////////////////////")
print("\n")

while check == "S": 
    email = input("proxima entrada: ").upper()  
    if re.match("[^@]+@[^@]+\.[^@]+", email):
        emails.append(email)
    else:
        print("erro de entrada, email invalido")
    
    check2 = ""
    while check2 != "S" and check2 != "N": 
        check2 = input("Deseja cadastrar outro email? S / N   ").upper()
    check = check2

check = "S"
while check == "S":
    achou = False
    emailValido = False

    print("\n")
    while emailValido == False:
        email = input("Digite o email a ser procurado:   ").upper()  
        if re.match("[^@]+@[^@]+\.[^@]+", email):
            emailAlvo = email
            emailValido = True
        else:
            print("erro de entrada, email invalido")
            emailValido = False

    for todosEmail in emails:
        if emailAlvo == todosEmail:
            print(todosEmail.lower())
            print("Email DETECTADO, voce foi exposto")
            print("\n")
            achou = True

    if achou == False:
        print("tudo safe campeão, nada foi vazado")
        print("\n")
    check2 = ""
    while check2 != "S" and check2 != "N": 
        check2 = input("Deseja fazer outra pesquisa? S / N   ").upper()
    check = check2
    achou = False

print("\n")
print("Obrigado por usar nossa solução ;) - tenha um otimo dia")
print("\n")
print("/////////////////----------------////////////////////////---------------////////////////////")
print("\n")
print("1TDCR NOITE   -------------- FIAP 2020")
print("\n")
print("/////////////////----------------////////////////////////---------------////////////////////")