# desafio 036 mundo 2 cusrso em video guanabara

valor= int(input('Valor da casa para Finaciamento ?'))
salario = int(input('Valor do seu salario bruto ? '))
anos = int(input('Quantos anos você pagara  ? '))
pmeses = (anos*12) 
pres_mês = (valor/pmeses)
if pres_mês > salario * 0.3: # modulo de como fazer os 30%  = valor *0.3
    print("Seu empretimo foi negado devido a prestcao ter ultrapaso os 30%, Obrigado!!")
else:
    print("seu finaciamneto foi aprovado, muito Obrigado !!")   