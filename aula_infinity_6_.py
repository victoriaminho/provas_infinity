usuario_correto = "admin"
senha_correta = "1234"


tentativas_restantes = 3


for tentativa in range(3):
    print(f"\nTentativa {tentativa + 1} de 3")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("\n✅ Login bem-sucedido. Bem-vindo!")
        break
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f"❌ Usuário ou senha incorretos. Tentativas restantes: {tentativas_restantes}")
        else:
            print("❌ Usuário ou senha incorretos.")


if tentativas_restantes == 0:
    for _ in range(3):
        print("🚫 Acesso bloqueado.")

