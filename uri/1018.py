V = int(input())

print (V)

a = int(V%100)
print (int(V/100), 'nota(s) de R$ 100,00')

b = int(a%50)
print (int (a/50), 'nota(s) de R$ 50,00')

c = int(b%20)
print (int (b/20), 'nota(s) de R$ 20,00')

d = int(c%10)
print (int (c/10), 'nota(s) de R$ 10,00')

e = int(d%5)
print (int (d/5), 'nota(s) de R$ 5,00')

f = int(e%2)
print (int (e/2), 'nota(s) de R$ 2,00')

g = int(f%1)
print (int (f/1), 'nota(s) de R$ 1,00')