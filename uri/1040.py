N1, N2, N3, N4 = input().split(" ")

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

#if media >= 5.0 and media < 7.0:
#    N5 = float(input())

print ('Media: %.1f' %media)

if media >= 7.0:
    print ("Aluno aprovado.")
elif media < 5.0:
    print ("Aluno reprovado.")
elif media >= 5.0 and media < 7.0:
    print ("Aluno em exame.")
    N5 = float(input())
    print ("Nota do exame: %.1f" %N5)
    novamedia = float((media+N5)/2)
    if novamedia >= 5.0:
        print ("Aluno aprovado.")
    elif novamedia < 5.0:
        print ("Aluno reprovado.")
    print ('Media final: %.1f' %novamedia)
