notas =  float(input())

cem = int(notas/100)
notas = notas - (cem * 100)

cinquenta = int(notas/50)
notas = notas - (cinquenta*50)

vinte = int(notas/20)
notas = notas - (vinte * 20)

dez = int(notas/10)
notas = notas -(dez *10)

cinco = int(notas/5)
notas = notas - (cinco*5)

dois = int(notas/2)
notas =  notas - (dois*2)

um = int(notas/1)
notas  = notas -(um *1)

notas = notas * 100

cinquentaC = int(notas / 50)
notas = int(notas - (cinquentaC * 50))

VinteCincoC = int(notas / 25)
notas = (notas- (VinteCincoC*25))

dezC = int(notas / 10)
notas = int(notas -(dezC*10))

cincoC = int(notas / 5)
notas = int(notas - (cincoC* 5))

umC =  int(notas/ 1)
notas = int(notas-(umC* 1))


print("NOTAS:")
print("{} nota(s) de R$ 100.00\n{} nota(s) de R$ 50.00".format(cem,cinquenta))
print("{} nota(s) de R$ 20.00\n{} nota(s) de R$ 10.00".format(vinte,dez))
print("{} nota(s) de R$ 5.00\n{} nota(s) de R$ 2.00".format(cinco,dois))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00\n{} moeda(s) de R$ 0.50".format(um,cinquentaC))
print("{} moeda(s) de R$ 0.25\n{} moeda(s) de R$ 0.10".format(VinteCincoC,dezC))
print("{} moeda(s) de R$ 0.05\n{} moeda(s) de R$ 0.01".format(cincoC,umC))
