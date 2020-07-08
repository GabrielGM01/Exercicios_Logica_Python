lista = []
for i in range(0,6):
   numeros = input()
   lista.append(float(numeros))  
lista_positiva = [x for x in lista if x > 0]
quantidade_positivo = len(lista_positiva)
print("{} valores positivos".format(quantidade_positivo)) 
   


