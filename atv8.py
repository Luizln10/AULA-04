soma = 0
media = 1
for i in range(1, 6):
    notas = float(input("Digite a nota do aluno:"))
    soma += notas
    media = soma / i

if media >= 6:
        print("Aprovado!")
else:
        print("Reprovado!")