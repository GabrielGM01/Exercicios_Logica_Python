"""Leia 3 valores inteiros e ordene-os em ordem crescente. 
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos."""

a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)
n1 = [a,b,c]
n2 = [a,b,c]
n1.sort(key=int)

print("{}\n{}\n{}\n".format(n1[0],n1[1],n1[2]))
print("{}\n{}\n{}".format(n2[0],n2[1],n2[2]))
