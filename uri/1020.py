N = int(input())

ano = int(N/365)
print(ano, "ano(s)")

mes = int((N%365)/30)
print(mes, "mes(es)")

dia = int((N%365)%30)
print(dia, "dia(s)")