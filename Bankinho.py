from datetime import datetime
datetime = datetime.now()
print(datetime)
menuPrincipal = (['Fazer um PIX', 'Histórico de Transações', 'Sair'])

def leiaInt(msg):
    while True:
        try: 
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: Por favor instira um valor válido")
            continue
        else:
            return n 


#Pegar valor do pix e pra quem mandar
#Registrar data e hora
#Armazenar essas informações dentro de algum lugar(p.o.o. talvez? class "pix"?)
def pix():
    global valor
    global pessoa
    global datahora
    valor = leiaInt("Qual é o valor do PIX?")
    pessoa = str(input("pra quem vc quer fazer o PIX?"))
    datahora = datetime.now()
    print(f'''Valor: {valor}
Pessoa: {pessoa}
Data e hora: {datahora}''')
    print("fim do processo")
    return valor, pessoa, datahora

def menu(texto):
    print("-="*16)
    c = 1
    for item in texto:
        print(f'{c} - {item}')
        c += 1
    print("-=" * 16)

while True:
    menu(menuPrincipal)
    resp = str(input("Sua Opção: "))
    if resp == "1":
        pix()

    elif resp == "2":
        print("Ainda n tá pronto")
    elif resp == "3":
        print("Adeus!")
        break
    else:
        print("ERRO: Digite uma opção válida")