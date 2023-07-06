nota1 = float(input("PRIMEIRA NOTA :"))
nota2 = float(input("SEGUNDA NOTA :"))
media = (nota1+nota2)/2
print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota1,nota2,media))
if media>7:
    print("O aluno está APROVADO")
elif media<5:
    print("O aluno está REPROVADO")
else:
     print("O aluno está em RECUPERCACÃO")
    