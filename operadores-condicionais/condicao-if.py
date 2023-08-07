def sacar(valor):
    saldo = 500
    cheque_especial =2000
    sim = True
    Não = False
    if saldo >= valor:
         print("valor sacado!")
         print("retire seu dinheiro do caixa")
    elif saldo < valor:
        print("Saldo insuficiente") 
        print("Deseja entrar no cheque especial?")
        if cheque_especial >= valor:
            print("Você entrou no cheque especial")
    print("Obrigado por ser nosso cliente, volte sempre!")
sacar(1000)