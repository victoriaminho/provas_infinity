# Solicita ao usuário o início e fim do intervalo
inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

soma_pares = 0
encontrou_par = False

# Loop que percorre o intervalo (inclusive)
for num in range(inicio, fim + 1):
    if num % 2 == 0:
        soma_pares += num
        encontrou_par = True
else:
    if not encontrou_par:
        print("Não há números pares no intervalo.")

 #Exibe o resultado
print(f"Soma dos números pares no intervalo: {soma_pares}")