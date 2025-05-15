
quantidade_alunos = int(input("Digite o número de alunos: "))


soma_das_medias = 0


for i in range(quantidade_alunos):
    print(f"\nAluno {i + 1}")
    
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    

    media = (nota1 + nota2 + nota3) / 3
    

    soma_das_medias += media
    

    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"
    

    print(f"Nome: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {status}")


media_geral = soma_das_medias / quantidade_alunos
print(f"\nMédia geral da turma: {media_geral:.2f}")
