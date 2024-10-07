import os  # Importação da biblioteca para limpeza do console.

from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

    # Função para calculo do preço final da reserva.
def calcular_preco(pessoas, tipo_apartamento, dias_reserva):
        precos = {
        
        #Utilizando uma estrutura de dicionário para a relação de pessoas e valores dos apartamentos
        
        '1': {1: 20.00, 2: 28.00, 3: 35.00, 4: 42.00, 5: 48.00, 6: 53.00},
        '2': {1: 25.00, 2: 34.00, 3: 42.00, 4: 50.00, 5: 57.00, 6: 63.00}
        }

        preco_por_pessoa = precos[tipo_apartamento].get(pessoas, 0)
        return preco_por_pessoa * pessoas * dias_reserva
    
    # Função para iniciar o processo de reserva
def fazer_reserva():
    while 1==1:
        try:
            # Pergunta o número de pessoas
            pessoas = int(input("Para quantas pessoas deseja fazer a reserva? (De 1 a 6 pessoas)"))
            if pessoas not in [1, 2, 3, 4, 5, 6]:
                print ("Número de pessoas não suportado.")
                input("Pressione Enter para voltar ao menu.")
                return
                
            os.system('cls')
            # Pergunta o tipo de apartamento
            tipo_apartamento = input('''
           
               Qual o tipo do apartamento?
               
               [1] TIPO 1 (1° Classe)
               [2] TIPO 2 (2° Classe)
               ==========> ''')

            if tipo_apartamento not in ['1', '2']:
                    os.system('cls')
                    print("Selecione uma opção válida")
                    input("Pressione enter para voltar ao menu.")
                    return

            
                # Pergunta o número de dias da reserva.
            os.system('cls')
            dias_reserva = int(input("Por quantos dias? ==> "))
            preco_total = calcular_preco(pessoas, tipo_apartamento, dias_reserva)


            # Exibe uma confirmação da reserva, valor total e mensagem de agradecimento.
            os.system('cls')
            print("RESERVA EFETUADA COM SUCESSO !!!")
            print(f"O valor total da estadia fica em R${preco_total:.2f}")
            print(f"RESUMO DA RESERVA\n Numero de pessoas:{pessoas}\n Apartamento Tipo:{tipo_apartamento}\nPor {dias_reserva} dias")
            print("OBRIGADO PELA PREFERÊNCIA !!!")
            input("Pressione Enter para voltar ao menu.")  # Pausa antes de voltar ao menu.

        except:
             print("Por favor, insira um valor numérico válido.")
             input("Pressione Enter para voltar.")  # Pausa antes de voltar.
             os.system('cls')
    
    
    # Função para exibir a tabela de preços
def tabela_precos():
        print('''
        TABELA DE PREÇOS:
        - Tipo 1:
            1 pessoa:  R$20,00/dia
            2 pessoas: R$28,00/dia
            3 pessoas: R$35,00/dia
            4 pessoas: R$42,00/dia
            5 pessoas: R$48,00/dia
            6 pessoas: R$53,00/dia
        - Tipo 2:
            1 pessoa:  R$25,00/dia
            2 pessoas: R$34,00/dia
            3 pessoas: R$42,00/dia
            4 pessoas: R$50,00/dia
            5 pessoas: R$57,00/dia
            6 pessoas: R$63,00/dia
        ''')
        input("Pressione Enter para voltar ao menu.")


    # Função para sair
def sair():
    print("FIM DO PROGRAMA")


# Criando o menu principal utilizando console-menu

menu = ConsoleMenu("Colônia de Férias da UMC", "Seja muito Bem Vindo!!!")


# Adicionando itens ao menu
menu.append_item(FunctionItem("Fazer Reserva", fazer_reserva))
menu.append_item(FunctionItem("Ver Tabela de Preços", tabela_precos))
menu.append_item(FunctionItem("Sair", sair))


menu.show()


