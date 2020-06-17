
DDDI = int(input())

DDD = [61,71,11,21,32,19,27,31]
En = ["Brasilia","Salvador","Sao Paulo","Rio de Janeiro",
    "Juiz de Fora","Campinas","Vitoria","Belo Horizonte"]
VI = DDDI in DDD
if(VI == False):
   print("DDD nao cadastrado")

else:
    VF = DDD.index(DDDI)
    print(En[VF])


