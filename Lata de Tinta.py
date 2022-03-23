print("{:^40}". format ("Loja de Tintas KOFITY"))
print()
metro = int(input("Qual a área em metros quadrados a ser pintada? "))
print()
litro = metro/3
tinta = litro/18
print("Será necessário", round(tinta+0.49), "lata(s) de tinta")
preco = round(tinta+0.49)*80
print("O preço final da(s) %.0f lata(s) de tinta é de R$ %.0f"%(tinta+0.49, preco))