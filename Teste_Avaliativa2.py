import os  # Importação da biblioteca para limpeza do console.

from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

    # Função para calculo do preço final da reserva.
def calcular_preco(pessoas, tipo_apartamento, dias_reserva):
        #Utilizando uma estrutura de dicionário para a relação de pessoas e valores dos apartamentos
        precos = {
        '1': {1: 20.00, 2: 28.00, 3: 35.00, 4: 42.00, 5: 48.00, 6: 53.00},
        '2': {1: 25.00, 2: 34.00, 3: 42.00, 4: 50.00, 5: 57.00, 6: 63.00}
        }
        
        preco_por_pessoa = precos[tipo_apartamento].get(pessoas, 0)
        return preco_por_pessoa * pessoas * dias_reserva
        
def cadastro_cliente():
        
        try:
            nome = (input ("Insira o seu nome: "))
            cpf = int (input ("Insira o numero do CPF: "))
            cidade = (input ("Qual sua cidade?: "))
            
            cor = '\033[1;37;42m'
            fim = '\033[0m'
            sucesso = 'Cadastro efetuado com sucesso!!!'
            bem_vindo = f'Seja bem vindo(a) {nome}'
            resumo_cpf = f'CPF: {cpf}'
            resumo_cidade = f'Cidade: {cidade}'
            print(f"{cor}{sucesso:^146}")
            print(f"{bem_vindo:^146}")
            print(f"{resumo_cpf:^146}")
            print(f"{resumo_cidade:^146}{fim}")
            input("Pressione Enter para voltar ao menu e fazer sua reserva no item 3.")

        
        except:
             print("Insira um valor válido!!!")
             input("Pressione Enter para voltar ao menu.")  
          

    
# Função para iniciar o processo de reserva
def fazer_reserva():
    while 1==1:
        try:
            # Pergunta o tipo de apartamento.
            tipo_apartamento = input('''
           
               Qual o tipo do apartamento?
               
               [1] TIPO 1 (2° Classe)
               [2] TIPO 2 (1° Classe)
               ==========> ''')

            if tipo_apartamento not in ['1', '2']:
                    os.system('cls')
                    print("Selecione uma opção válida")
                    input("Volte ao menu e tente novamente.")
                    return
            
            # Pergunta o número de pessoas
            os.system('cls')
            pessoas = int(input("Para quantas pessoas deseja fazer a reserva? (De 1 a 6 pessoas)=====>"))
            if pessoas not in [1, 2, 3, 4, 5, 6]:
                print ("Número de pessoas não suportado.")
                input("Volte ao menu e tente novamente.")
                return
                
                
                    

            
            # Pergunta o número de dias da reserva e calcula seu preço total.
            os.system('cls')
            dias_reserva = int(input("Por quantos dias? ==> "))
            preco_total = calcular_preco(pessoas, tipo_apartamento, dias_reserva)


            # Exibe uma confirmação da reserva, valor total e mensagem de agradecimento.
            os.system('cls')
            print("RESERVA EFETUADA COM SUCESSO !!!")
            print(f"O valor total da reserva fica em R${preco_total:.2f}")
            print(f"RESUMO DA RESERVA\nNumero de pessoas:{pessoas}\nApartamento Tipo:{tipo_apartamento}\nPor {dias_reserva} dia(s)")
            print("Cadastro efetuado com sucesso!!!")
            print("OBRIGADO PELA PREFERÊNCIA !!!")
            input("Pressione Enter para voltar ao menu.")  # Pausa antes de voltar ao menu.
            break

        except:
             print("Por favor, insira um valor numérico.")
             input("Pressione Enter para voltar.")  # Pausa antes de voltar ao menu.
    
    
    # Função para exibir a tabela de preços.
def tabela_precos():
        print('''
        TABELA DE PREÇOS:
            VALORES POR PESSOA!!!
        - Tipo 1: (2ª Classe)
            1 pessoa:  R$ 20,00/dia
            2 pessoas: R$ 28,00/dia
            3 pessoas: R$ 35,00/dia
            4 pessoas: R$ 42,00/dia
            5 pessoas: R$ 48,00/dia
            6 pessoas: R$ 53,00/dia
        - Tipo 2: (1ª Classe)
            1 pessoa:  R$ 25,00/dia
            2 pessoas: R$ 34,00/dia
            3 pessoas: R$ 42,00/dia
            4 pessoas: R$ 50,00/dia
            5 pessoas: R$ 57,00/dia
            6 pessoas: R$ 63,00/dia
        ''')
        input("Pressione Enter para voltar ao menu.")




# Criando o menu principal utilizando console-menu.

menu = ConsoleMenu("Colônia de Férias da UMC", "Seja muito Bem Vindo!!!")


# Adicionando itens ao menu.
menu.append_item(FunctionItem("Cadastro", cadastro_cliente))
menu.append_item(FunctionItem("Fazer Reserva", fazer_reserva))
menu.append_item(FunctionItem("Ver Tabela de Preços", tabela_precos))


menu.show()