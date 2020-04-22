"""Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”"""

a,b,c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

if(a >= b and a >= c):
  print("{} eh o maior".format(a))
elif( b >= a and b >= c):
  print("{} eh o maior".format(b))
elif(c >= a and c >= b):
  print("{} eh o maior".format(c))
else:
  print("erro")