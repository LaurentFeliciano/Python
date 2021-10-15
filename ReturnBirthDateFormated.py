# crie um script em python que leia o dia, 
# o mês e o ano de nascimento de uma pessoa 
# e mostre uma mensagem com a data formatada
def FormatarData():
    '''That Function returns Birth Date of user in DateTime format.  '''
    import datetime
    while True:
        try:
            DataAtual= datetime.datetime.now()
            Ano=input('Digite o ano do seu nascimento(formato ####):')
            while len(Ano) != 4 or int(Ano)> DataAtual.year :
                Ano=input('Digite o ano do seu nascimento da maneira correta(formato ####):')
            Mes=input('Digite o mês do seu nascimento(formato #):')
            while len(Mes) < 1 or len(Mes) > 2 or int(Mes)> 12 or int(Mes)<1 :
                Mes=input('Digite o mês do seu nascimento da maneira correta(formato #):')  

            Dia = input('Digite o dia do seu nascimento(formato ## ou #):')
            while len(Dia) < 1 or len(Dia) > 2:
                Dia = input('Digite o dia do seu nascimento da maneira correta(formato ## ou #):')
            Data = datetime.datetime(int(Ano),int(Mes),int(Dia))
            return Data
        except Exception as erro:
            print(f'Erro: {erro}')
