"""Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, 
   e informe-o expresso no formato horas:minutos:segundos."""



numero = int(input())
hora = numero // 60**2
numero = numero - hora * 60**2

minuto = numero // 60
numero = numero - minuto*60

segundos = numero

print('{}:{}:{}'.format(hora, minuto, segundos))


