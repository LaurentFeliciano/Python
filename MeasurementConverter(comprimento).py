# Escreva um programa que leia um valor em metros e o 
# exiba convertido em centímetros e milímetros.
def MeasurementConverter(Value):
    while True:
        try:
            Question = float(input('''
            Painel de conversões de medidas(A partir do metro):
            Comprimento:
            Quilômetro(km) – [1]
            Hectômetro(hm) – [2]
            Decâmetro (dam)– [3]
            Metro     (m)  – [4]
            decímetro (dm) – [5]
            centímetro(cm) – [6]
            milímetro (mm) – [7]
            Deseja converter para qual das medidas acima:'''))
            while Question <1 or Question>7:
                Question = float(input('Digite um dos números acima:'))
            if Question== 1:
                Measure= 'km'
                Answer = Value/1000
            elif Question ==2:
                Answer = Value/100
                Measure= 'hm'
            elif Question ==3:
                Answer = Value/10
                Measure= 'dam'
            elif Question ==4:
                Answer = Value/1
                Measure= 'm'
            elif Question ==5:
                Answer = Value*10
                Measure= 'dm'
            elif Question ==6:
                Answer = Value*100
                Measure= 'cm'
            elif Question ==7:
                Answer = Value*1000
                Measure= 'mm'
            return Answer,Measure
        except Exception as Error: print(f'Erro:{Error}')
