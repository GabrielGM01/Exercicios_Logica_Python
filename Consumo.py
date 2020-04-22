"""Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros)."""

x = int(input())
y = float(input())

M = x/y

print("{:.3f} km/l".format(M))
