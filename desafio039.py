# FICHA PARA SOBRE SEU ALISTAMENTO 
from datetime import date
atual = date.today().year
nasc = int(input("ANO DE NASCIMENTO: "))
idade = atual - nasc
print(f"QUEM NASCE EM {nasc} TEM {idade} ANOS EM {atual}")
if idade == 18:
    print("VOCE TEM QUE SE ALISTAR IMEDIATAMENTE !!")   
elif idade < 18:
    saldo = 18 - idade
    print(f"AINDA FALTA {saldo} ANOS PARA O ALISTAMENTO")
    ano = atual + saldo
    print(f"SEU ALISTAMENTO SERA EM {ano}")
elif idade > 18:
    saldo = idade - 18
    print(f"VOCE JA DEVERIA TER SE ALISTADO HA {saldo} ANOS")
    ano = atual - saldo 
    print(f"SEU ALISTAMENTO FOI EM {ano}") 