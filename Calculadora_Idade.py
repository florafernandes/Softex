n=1

try:
    while n!=0:
        nome = str(input("Digite seu nome: "))
        ano_nascimento= int(input("Digite seu ano de nascimento: "))

        if ano_nascimento>1922 and ano_nascimento<2021:
            ano_atual=2022
            idade= ano_atual - ano_nascimento
            print ("Olá ",nome, "sua idade atual é", idade, "anos")
        else:
            print ("Insira um ano entre 1922 e 2021.")
except ValueError:
    print ('Insira um valor válido')