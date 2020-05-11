n1,n2,n3 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

m = [n1,n2,n3]
m.sort(reverse=True)
A = m[0]
B = m[1]
C = m[2]

if(A >= B+C):
    print("NAO FORMA TRIANGULO")
elif(A**2 == B**2+C**2):
   print("TRIANGULO RETANGULO")
elif(A**2 > B**2+C**2):
    print("TRIANGULO OBTUSANGULO")
    if(A == B and B == C):
       print("TRIANGULO EQUILATERO")
    elif(A == B or  A == C or B == A or B == C  or C == A or C == B ):
       print("TRIANGULO ISOSCELES")

elif(A**2 < B**2 + C**2):
   print("TRIANGULO ACUTANGULO")
   if(A == B and B == C):
      print("TRIANGULO EQUILATERO")
   elif(A == B or  A == C or B == A or B == C  or C == A or C == B ):
      print("TRIANGULO ISOSCELES")
       
