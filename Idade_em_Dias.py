"""Leia um valor inteiro correspondente à idade de uma pessoa em dias 
   e informe-a em anos, meses e dias"""




idade = int(input())

ano = 365
mes = 30

ano_T = int( idade / ano)
idade = idade - ano_T*365
mes_T = int(idade / mes)
idade = idade - mes_T*30
dias = idade

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ano_T,mes_T,dias))