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
            nome = (input ("Insira um usuário: "))
            cpf = int (input ("Insira o numero do CPF (apenas números): "))
            cidade = (input ("Qual sua cidade?: "))
            
            os.system('cls')
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
            espaco = ''
            Tabela_preco = 'TABELA DE PREÇOS'
            atencao = '!!!VALORES POR PESSOA!!!'
            # Apartamento Tipo 1
            Tipo1 = '- Tipo 1: (2ª Classe)'
            T1P1 =  '1 pessoa:  R$ 20,00/dia'
            T1P2 =  '2 pessoas: R$ 28,00/dia'
            T1P3 =  '3 pessoas: R$ 35,00/dia'
            T1P4 =  '4 pessoas: R$ 42,00/dia'
            T1P5 =  '5 pessoas: R$ 48,00/dia'
            T1P6 =  '6 pessoas: R$ 53,00/dia'

            # Apartamento Tipo 2
            Tipo2 = '- Tipo 2: (1ª Classe)'
            T2P1 =  '1 pessoa:  R$ 25,00/dia'
            T2P2 =  '2 pessoas: R$ 34,00/dia'
            T2P3 =  '3 pessoas: R$ 42,00/dia'
            T2P4 =  '4 pessoas: R$ 50,00/dia'
            T2P5 =  '5 pessoas: R$ 57,00/dia'
            T2P6 =  '6 pessoas: R$ 63,00/dia'

            print (f'{espaco:-^146}')
            print (f"|{Tabela_preco:^146}|")
            print (f"|{atencao:^146}|")
            print (f'{espaco:-^146}')
            print (f"|{Tipo1:^50}|{Tipo2:^49}|")
            print (f'|{espaco:^146}|')
            print (f"|{T1P1:^50}|{T2P1:^49}|")
            print (f"|{T1P2:^50}|{T2P2:^49}|")
            print (f"|{T1P3:^50}|{T2P3:^49}|")
            print (f"|{T1P4:^50}|{T2P4:^49}|")
            print (f"|{T1P5:^50}|{T2P5:^49}|")
            print (f"|{T1P6:^50}|{T2P6:^49}|")
            print (f'|{espaco:^146}|')
            print (f'{espaco:-^146}')

            tipo_apartamento = input("Qual o tipo do apartamento? ")
            
            if tipo_apartamento not in ['1', '2']:
                    
                    print("Selecione uma opção válida")
                    input("Aperte Enter para voltar ao menu e tente novamente.")
                    return
            
            # Pergunta o número de pessoas
            
            
            pessoas = int(input("Para quantas pessoas (1-6) deseja fazer a reserva? "))
            
            if pessoas not in [1, 2, 3, 4, 5, 6]:
                print ("Número de pessoas não suportado.")
                input("Volte ao menu e tente novamente.")
                return
                
                
                    

            
            # Pergunta o número de dias da reserva e calcula seu preço total.
            
            dias_reserva = int(input("Por quantos dias (ilimitado)?  "))
            
            preco_total = calcular_preco(pessoas, tipo_apartamento, dias_reserva)


            # Exibe uma confirmação da reserva, valor total e mensagem de agradecimento.
            os.system('cls')
            espaco = ''
            reserva_sucesso = f'Reserva efetuada com sucesso!!!'
            total_reserva = f'O valor total da reserva fica em R$ {preco_total:.2f}'
            resumo_reserva = 'RESUMO DA RESERVA'
            num_pessoas = f'Numero de Pessoas: {pessoas}'
            apartamento_tipo = f'Apartamento Tipo: {tipo_apartamento}'
            resumo_dias = f'Por {dias_reserva} dia(s)'
            obrigado = f'OBRIGADO PELA PREFERÊNCIA !!!'
            print (f"-{espaco:-^200}-")
            print(f"|{reserva_sucesso:^200}|")
            print (f"|{espaco:-^200}|")
            print (f"|{resumo_reserva:^200}|")
            print(f"|{num_pessoas:^200}|")
            print(f"|{apartamento_tipo:^200}|")
            print(f"|{resumo_dias:^200}|")
            print(f"|{total_reserva:^200}|")
            print (f"|{espaco:-^200}|")
            print(f"|{obrigado:^200}|")
            print (f"-{espaco:-^200}-")
            input("Pressione Enter para voltar ao menu.")  # Pausa antes de voltar ao menu.
            break


        except:
             print("Por favor, insira um valor numérico.")
             input("Pressione Enter para voltar.")  # Pausa antes de voltar ao menu.
             os.system('cls')
    
    
# Função para exibir a tabela de preços de forma independente.
def tabela_precos():
            espaco = ''
            Tabela_preco = 'TABELA DE PREÇOS'
            atencao = '!!!VALORES POR PESSOA!!!'
            # Apartamento Tipo 1
            Tipo1 = '- Tipo 1: (2ª Classe)'
            T1P1 =  '1 pessoa:  R$ 20,00/dia'
            T1P2 =  '2 pessoas: R$ 28,00/dia'
            T1P3 =  '3 pessoas: R$ 35,00/dia'
            T1P4 =  '4 pessoas: R$ 42,00/dia'
            T1P5 =  '5 pessoas: R$ 48,00/dia'
            T1P6 =  '6 pessoas: R$ 53,00/dia'

            # Apartamento Tipo 2
            Tipo2 = '- Tipo 2: (1ª Classe)'
            T2P1 =  '1 pessoa:  R$ 25,00/dia'
            T2P2 =  '2 pessoas: R$ 34,00/dia'
            T2P3 =  '3 pessoas: R$ 42,00/dia'
            T2P4 =  '4 pessoas: R$ 50,00/dia'
            T2P5 =  '5 pessoas: R$ 57,00/dia'
            T2P6 =  '6 pessoas: R$ 63,00/dia'

            print (f'{espaco:-^202}')
            print (f"|{Tabela_preco:^200}|")
            print (f"|{atencao:^200}|")
            print (f'{espaco:-^202}')
            print (f"|{Tipo1:^100}|{Tipo2:^99}|")
            print (f'|{espaco:^200}|')
            print (f"|{T1P1:^100}|{T2P1:^99}|")
            print (f"|{T1P2:^100}|{T2P2:^99}|")
            print (f"|{T1P3:^100}|{T2P3:^99}|")
            print (f"|{T1P4:^100}|{T2P4:^99}|")
            print (f"|{T1P5:^100}|{T2P5:^99}|")
            print (f"|{T1P6:^100}|{T2P6:^99}|")
            print (f'|{espaco:^200}|')
            print (f'{espaco:-^202}')
            input("Pressione Enter para voltar ao menu.")




# Criando o menu principal utilizando console-menu.

menu = ConsoleMenu("Colônia de Férias da UMC", "Seja muito Bem Vindo!!!")


# Adicionando itens ao menu.
menu.append_item(FunctionItem("Cadastro", cadastro_cliente))
menu.append_item(FunctionItem("Ver Tabela de Preços", tabela_precos))
menu.append_item(FunctionItem("Fazer Reserva", fazer_reserva))


menu.show()