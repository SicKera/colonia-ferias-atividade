import os  # Importação da biblioteca para limpeza do console.
# Importação da biblioteca console-menu.
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
    # Função para cadastro de clientes.    
def cadastro_cliente():
        
        try:
            nome = (input ("Insira um usuário: "))
            cpf = int (input ("Insira o numero do CPF (apenas números): "))
            cidade = (input ("Qual sua cidade?: "))
            
            os.system('cls')
            cor_sucesso = '\033[1;37;42m'
            cor_texto = '\033[7;37;40m'
            fim = '\033[0m'
            espaco = ''
            sucesso = 'Cadastro efetuado com sucesso!!!'
            bem_vindo = f'Seja bem vindo(a) {nome} !!!'
            resumo_cpf = f'CPF: {cpf}'
            resumo_cidade = f'Cidade: {cidade}'
            print (f'{cor_sucesso}{espaco:-^120}')
            print(f"|{sucesso:^118}|")
            print (f'{espaco:-^120}{fim}')
            print(f"{cor_texto}|{bem_vindo:^118}|")
            print(f"|{resumo_cpf:^118}|")
            print(f"|{resumo_cidade:^118}|")
            print (f'{espaco:-^120}{fim}')
            input("Pressione Enter para voltar ao menu e fazer sua reserva no item 3.")

        
        except:
             cor_erro = '\033[1;50;41m'
             fim = '\033[0m'
             os.system('cls')
             print(f"{cor_erro}Insira um valor válido!!!{fim}")
             input("Pressione Enter para voltar ao menu e tente novamente.")
             
          

    
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

            cor = '\033[7;37;40m'
            fim = '\033[0m'
            print (f'{cor}{espaco:-^102}')
            print (f"|{Tabela_preco:^100}|")
            print (f"|{atencao:^100}|")
            print (f'{espaco:-^102}')
            print (f"|{Tipo1:^50}|{Tipo2:^49}|")
            print (f'|{espaco:^100}|')
            print (f"|{T1P1:^50}|{T2P1:^49}|")
            print (f"|{T1P2:^50}|{T2P2:^49}|")
            print (f"|{T1P3:^50}|{T2P3:^49}|")
            print (f"|{T1P4:^50}|{T2P4:^49}|")
            print (f"|{T1P5:^50}|{T2P5:^49}|")
            print (f"|{T1P6:^50}|{T2P6:^49}|")
            print (f'|{espaco:^100}|')
            print (f'{espaco:-^102}{fim}')

            tipo_apartamento = input("Qual o tipo do apartamento? ")
            
            if tipo_apartamento not in ['1', '2']:
                    
                    cor_erro = '\033[1;50;41m'
                    fim = '\033[0m'
                    os.system('cls')
                    print(f"{cor_erro}Opção inválida!!!{fim}")
                    input("Aperte Enter para voltar e tente novamente.")
                    os.system('cls')
                    continue
            
            
            
            # Pergunta o número de pessoas
            pessoas = int(input("Para quantas pessoas (1-6) deseja fazer a reserva? "))
            
            if pessoas not in [1, 2, 3, 4, 5, 6]:
                cor_erro = '\033[1;50;41m'
                fim = '\033[0m'
                os.system('cls')
                print (f"{cor_erro}Número de pessoas não suportado.{fim}")
                input("Aperte Enter para voltar.")
                os.system('cls')
                continue
                
                
                    

            
            
            # Pergunta o número de dias da reserva e calcula seu preço total.
            dias_reserva = int(input("Por quantos dias (ilimitado)?  "))
            
            preco_total = calcular_preco(pessoas, tipo_apartamento, dias_reserva)


            # Exibe uma confirmação da reserva, valor total e mensagem de agradecimento.
            os.system('cls')
            cor_sucesso = '\033[1;37;42m'
            cor_texto = '\033[7;37;40m'
            fim = '\033[0m'
            espaco = ''
            reserva_sucesso = f'Reserva efetuada com sucesso!!!'
            total_reserva = f'O valor total da reserva fica em R$ {preco_total:.2f}'
            resumo_reserva = 'RESUMO DA RESERVA'
            num_pessoas = f'Numero de Pessoas: {pessoas}'
            apartamento_tipo = f'Apartamento Tipo: {tipo_apartamento}'
            resumo_dias = f'Por {dias_reserva} dia(s)'
            obrigado = f'OBRIGADO PELA PREFERÊNCIA !!!'
            print (f"{cor_sucesso}-{espaco:-^100}-")
            print(f"|{reserva_sucesso:^100}|")
            print (f"|{espaco:-^100}|{fim}")
            print (f"{cor_texto}|{resumo_reserva:^100}|")
            print(f"|{num_pessoas:^100}|")
            print(f"|{apartamento_tipo:^100}|")
            print(f"|{resumo_dias:^100}|")
            print(f"|{total_reserva:^100}|")
            print (f"|{espaco:-^100}|")
            print(f"|{obrigado:^100}|")
            print (f"-{espaco:-^100}-{fim}")
            input("Pressione Enter para voltar ao menu.")  # Pausa antes de voltar ao menu.
            break


        except:
             cor_erro = '\033[1;50;41m'
             fim = '\033[0m'
             os.system('cls')
             print(f"{cor_erro}Entrada de dados inválida!!!.{fim}")
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

            cor = '\033[7;37;40m'
            fim = '\033[0m'
            print (f'{cor}{espaco:-^102}')
            print (f"|{Tabela_preco:^100}|")
            print (f"|{atencao:^100}|")
            print (f'{espaco:-^102}')
            print (f"|{Tipo1:^50}|{Tipo2:^49}|")
            print (f'|{espaco:^100}|')
            print (f"|{T1P1:^50}|{T2P1:^49}|")
            print (f"|{T1P2:^50}|{T2P2:^49}|")
            print (f"|{T1P3:^50}|{T2P3:^49}|")
            print (f"|{T1P4:^50}|{T2P4:^49}|")
            print (f"|{T1P5:^50}|{T2P5:^49}|")
            print (f"|{T1P6:^50}|{T2P6:^49}|")
            print (f'|{espaco:^100}|')
            print (f'{espaco:-^102}{fim}')
            input("Pressione Enter para voltar ao menu.")




# Criando o menu principal utilizando console-menu.
menu = ConsoleMenu("Colônia de Férias da UMC", "Seja muito Bem Vindo!!!")

# Adicionando itens ao menu.
menu.append_item(FunctionItem("Cadastro", cadastro_cliente))
menu.append_item(FunctionItem("Ver Tabela de Preços", tabela_precos))
menu.append_item(FunctionItem("Fazer Reserva", fazer_reserva))


menu.show()