"""
Coleta de leituras de velocidade do motor.
Receber 5 leituras, armazenar em lista
Funções para média, maior, menor e total
Relatório final organizado
Perguntar se deseja nova coleta
"""
l = []

while True:
    try:
        vel_motor = float(input('Digite 1 para iniciar ou 2 para encerrar: '))
        if vel_motor == 1:
            for i in range(5):
                vel_motor = float(input(f'Digite a velocidade do motor {i+1}: '))
                l.append(vel_motor)
            media = sum(l) / len(l)
            maior = max(l)
            menor = min(l)
            total = sum(l)

            print("Relatório Final:")
            print("-----------------")
            print('Média:',media)
            print('Maior:',maior)
            print('Menor:',menor)
            print('Total:',total)
            print("-----------------")
            l.clear()
        elif vel_motor == 2:
            print('Encerrando programa')
            break
        else:
            print('Opção inválida. Tente novamente')
    except ValueError:
        print('Entrada inválida. Por favor, digite um número válido')
        continue