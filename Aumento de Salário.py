
salario = float(input())
if(salario >=0 and salario <= 400.00):
    R = (salario * 15) / 100
    NS = salario + R
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 15 %".format(NS,R))
elif(salario >=400.01 and salario <= 800.00):
    R = (salario * 12) / 100
    NS = salario + R
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 12 %".format(NS,R))
elif(salario >=800.01 and salario <= 1200.00):
    R = (salario * 10) / 100
    NS = salario + R
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 10 %".format(NS,R))
elif(salario >=1200.01 and salario <= 2000.00):
    R = (salario * 7) / 100
    NS = salario + R
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 7 %".format(NS,R))
else:
    R = (salario * 4) / 100
    NS = salario + R
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 4 %".format(NS,R))
