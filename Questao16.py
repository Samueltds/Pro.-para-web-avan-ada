valor,taxa,tempo=float(input("Digite o valor da prestação:")),float(input("Digite a taxa da prestação:")),int(input("Digite o tempo da prestação em meses:"))
resultado=valor+(valor*(taxa/100)*tempo)
print("O valor desta prestação em atraso é %2.f:"%resultado)
