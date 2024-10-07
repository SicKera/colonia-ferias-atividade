import os  # Importação da biblioteca para limpeza do console.

while 1==1:  # Inicia um loop para o menu principal
    
    # Limpando o console.
    os.system("cls")

    # Menu Principal de opções.
    
    menu = input('''
        SEJA BEM VINDO À COLONIA DE FÉRIAS!!!
        DESEJA FAZER UMA RESERVA?
        [1] FAZER RESERVA
        [2] TABELA DE PREÇOS
        [3] SAIR
        ========> ''')

    # Criando as condições do menu de reserva.
    
    if menu not in ['1', '2', '3']:
        print("Selecione uma opção válida")
        input("Pressione Enter para voltar ao menu.")
    elif menu == '2':
        print("Obrigado por acessar e até a próxima!!!")
        break  # Sai do loop principal e finaliza o programa
    elif menu == '3':
        print("FIM DO PROGRAMA")
        break  # Sai do loop principal e finaliza o programa
    else:
        try:
            # Pergunta o número de pessoas
            pessoas = int(input("Para quantas pessoas deseja fazer a reserva? "))
            if pessoas not in [1, 2, 3, 4, 5, 6]:
                print ("Número de pessoas não suportado.")
                input("Pressione Enter para voltar ao menu.")
                continue
                

            # Pergunta o tipo de apartamento
            tipo_apartamento = input('''
           
               Qual o tipo do apartamento?
               
               [1] TIPO 1
               [2] TIPO 2
               ==========> ''')

            if tipo_apartamento not in ['1', '2']:
                    print("Selecione uma opção válida")
                    input("Pressione enter para voltar ao menu.")

            else:
                # Pergunta o número de dias da reserva.
                dias_reserva = int(input("Por quantos dias? ==> "))

                # Calcula o preço com base no número de pessoas, tipo de apartamento e dias de reserva.
                if pessoas == 1 and tipo_apartamento == '1':
                    preco = float(pessoas * 20.00) * dias_reserva
                elif pessoas == 2 and tipo_apartamento == '1':
                    preco = float(pessoas * 28.00) * dias_reserva
                elif pessoas == 3 and tipo_apartamento == '1':
                    preco = float(pessoas * 35.00) * dias_reserva
                elif pessoas == 4 and tipo_apartamento == '1':
                    preco = float(pessoas * 42.00) * dias_reserva
                elif pessoas == 5 and tipo_apartamento == '1':
                    preco = float(pessoas * 48.00) * dias_reserva
                elif pessoas == 6 and tipo_apartamento == '1':
                    preco = float(pessoas * 53.00) * dias_reserva
                elif pessoas == 1 and tipo_apartamento == '2':
                    preco = float(pessoas * 25.00) * dias_reserva
                elif pessoas == 2 and tipo_apartamento == '2':
                    preco = float(pessoas * 34.00) * dias_reserva
                elif pessoas == 3 and tipo_apartamento == '2':
                    preco = float(pessoas * 42.00) * dias_reserva
                elif pessoas == 4 and tipo_apartamento == '2':
                    preco = float(pessoas * 50.00) * dias_reserva
                elif pessoas == 5 and tipo_apartamento == '2':
                    preco = float(pessoas * 57.00) * dias_reserva
                elif pessoas == 6 and tipo_apartamento == '2':
                    preco = float(pessoas * 63.00) * dias_reserva
                

                # Exibe uma confirmação da reserva, valor total e mensagem de agradecimento.
                print("RESERVA EFETUADA COM SUCESSO !!!")
                print(f"O valor total da estadia fica em R${preco:.2f}")
                print("OBRIGADO PELA PREFERÊNCIA !!!")
                input("Pressione Enter para voltar ao menu.")  # Pausa antes de voltar ao menu.

        except:
            print("Por favor, insira um valor numérico válido.")
            input("Pressione Enter para voltar ao menu.")  # Pausa antes de voltar ao menu.

