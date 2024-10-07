# UMC
# Atividade Avaliativa 1
# Airton Siqueira da Cunha

import os                # <--------  importação de biblioteca para limpeza do console.



os.system("cls")
menu = input('''
        SEJA BEM VINDO À COLONIA DE FÉRIAS!!!
        DESEJA FAZER UMA RESERVA?
        [1] SIM
        [2] NÃO
        [3] SAIR
        ========> ''')
    
    # Criando as condições do menu de reserva.

if menu not in ['1', '2', '3']:
            print ("Selecione uma opção válida")
            input ("Pressione Enter para voltar ao menu.")
elif menu == '2':
            print ("Obrigado por acessar e até a próxima!!!")
elif menu == '1':
        try:
            pessoas = int (input("Para quantas pessoas deseja fazer a reserva? "))
        except:
            print ("Por favor entrar com valor numérico")
elif menu == '3':
            print ("FIM DO PROGRAMA")
    
    # Tipo do apartamento
else:
        tipo_apartamento = input ('''
           
           Qual o tipo do apartamento?
           
           [1] TIPO 1
           [2] TIPO 2
           ==========> ''')
    
        if tipo_apartamento not in ['1', '2']:
            print ("Selecione uma opção válida")
            input ("Pressione Enter para voltar.")

    # Dias de reserva e calculo do preço
        
        dias_reserva = int (input ("Por quantos dias? ==>"))

        if pessoas == 1 and tipo_apartamento == '1':
                preco = float (pessoas*20.00) * dias_reserva
        elif pessoas == 2 and tipo_apartamento == '1':
                preco = float (pessoas*28.00) * dias_reserva
        elif pessoas == 3 and tipo_apartamento == '1':
                preco = float (pessoas*35.00) * dias_reserva
        elif pessoas == 4 and tipo_apartamento == '1':
                preco = float (pessoas*42.00) * dias_reserva
        elif pessoas == 5 and tipo_apartamento == '1':
                preco = float (pessoas*48.00) * dias_reserva
        elif pessoas == 6 and tipo_apartamento == '1':
                preco = float (pessoas*53.00) * dias_reserva
        elif pessoas == 1 and tipo_apartamento == '2':
                preco = float (pessoas*25.00) * dias_reserva
        elif pessoas == 2 and tipo_apartamento == '2':
                preco = float (pessoas*34.00) * dias_reserva
        elif pessoas == 3 and tipo_apartamento == '2':
                preco = float (pessoas*42.00) * dias_reserva
        elif pessoas == 4 and tipo_apartamento == '2':
                preco = float (pessoas*50.00) * dias_reserva
        elif pessoas == 5 and tipo_apartamento == '2':
                preco = float (pessoas*57.00) * dias_reserva
        elif pessoas == 6 and tipo_apartamento == '2':
                preco = float (pessoas*63.00) * dias_reserva

print ("RESERVA EFETUADA COM SUCESSO !!!")
print ("O valor total da estadia fica em %.2f" %(preco))
print ("OBRIGADO PELA PREFERÊNCIA !!!")
    
    


    
    



           



