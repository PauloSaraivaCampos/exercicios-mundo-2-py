#conversao de bases

ent=int(input("DIGITE UM NÚMERO INTEIRO:"))
print("ESCOLHA UMA DAS BASES PARA PARA CONVERSÃO:")
print("[1] Converter para BINÁRIO")
print("[2] Converter para OCTANAL")
print("[3] Converter para HEXADECIMAL")
osp=int(input("SUA OPCAO:"))
if (osp == 1):
    print(f"{ent} convertido para BINÁRIO é igual a {bin(ent)}")
elif(osp==2):
    print(f"{ent} convertido para OCTANAL é igual a {oct(ent)}")
elif(osp==3):
    print(f"{ent} convertido para HEXADECIMAL é igual a {hex(ent)}")    
            