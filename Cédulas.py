"""Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
   As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
   A seguir mostre o valor lido e a relação de notas necessárias."""


valor = int(input())
print(valor)
cem = int(valor//100)
valor = valor-(cem*100)
cinquenta = int(valor//50)
valor = valor - (cinquenta*50)
vinte = int(valor//20)
valor = valor - (vinte*20)
dez = int(valor//10)
valor = valor - (dez*10)
cinco = int(valor//5)
valor = valor - (cinco*5)
dois =  int(valor//2)
valor =  valor - (dois*2)
um =  int(valor//1)
valor = valor - (um*1)


print("{} notas (s) de R$ 100,00".format(cem))
print("{} notas (s) de R$ 50,00".format (cinquenta)) 
print("{} notas (s) de R$ 20,00".format(vinte)) 
print("{} notas (s) de R$ 10,00".format(dez))
print("{} notas (s) de R$ 5,00".format(cinco)) 
print("{} notas (s) de R$ 2,00".format(dois))
print("{} notas (s) de R$ 1,00".format(um))
