
# Entrada de dados
entrada = input("")

notas = entrada.split()

soma_media = 0

for i in range(len(notas)):
    soma_media += float(notas[i])

media = soma_media/len(notas)


if(media >= 7.0):
    print("Aluno aprovado.")

elif(media < 7.0 and media > 5):
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame: ", nota_exame)
    media = (media + nota_exame)/2
    if(media >= 5.0):
        print("Aluno aprovado.")
        print("Media final: ", int(media))
    else:
        print("Aluno reprovado.")
else:
    print("Aluno reprovado.")
