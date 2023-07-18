"""
As regras são simples:

Tesoura corta Papel
Papel cobre Pedra
Pedra esmaga Lagarto
Lagarto envenena Spock
Spock esmaga Tesoura
Tesoura decapita Lagarto
Lagarto come Papel
Papel refuta Spock
Spock vaporiza Pedra
Pedra esmaga Tesoura

"""
"""
Esse jogo é inspirado em uma versão do
Pedra, Papel e Tesoura criado pelo personagem
Dr. Sheldon Lee Cooper da série The Big Bang Theory
(minha série favorita desde que assisti pela primeira vez)
onde aqui temos dois personagens adicionais:
 - Lagarto
 - Spock
O personagem Spock é o famoso Spock da franquia Star Trek
(uma das minhas favoritas). 

Divirta-se!

Vida Longa e Próspera!!
"""
import random

def jogo_pedra_papel_tesoura_lagarto_spock(jogador1, jogador2):
    opcoes = ["pedra", "papel", "tesoura", "lagarto", "spock"]

    if jogador1 not in opcoes or jogador2 not in opcoes:
        return "Opção inválida. Escolha entre pedra, papel, tesoura, lagarto ou spock."

    if jogador1 == jogador2:
        return "Empate!"

    vitorias = {
        "pedra": ["tesoura", "lagarto"],
        "papel": ["pedra", "spock"],
        "tesoura": ["papel", "lagarto"],
        "lagarto": ["papel", "spock"],
        "spock": ["pedra", "tesoura"]
    }

    if jogador2 in vitorias[jogador1]:
        return "Parabéns! Você venceu!"
    else:
        return "O Computador venceu!"
print("")
def exibir_menu_principal():
    
    print("Bem-vindo ao jogo de Pedra, Papel, Tesoura, Lagarto e Spock!")
    print("1. Jogar")
    print("2. Como Jogar")
    print("3. Introdução")
    print("4. Sair")
    print("")
def exibir_regras():
    print("")
    print("Essas são as opções: ")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    print("4. Lagarto")
    print("5. Spock")
    print("")
    print("Regras do Jogo:")
    print("Tesoura corta Papel")
    print("Papel cobre Pedra")
    print("Pedra esmaga Lagarto")
    print("Lagarto envenena Spock")
    print("Spock esmaga Tesoura")
    print("Tesoura decapita Lagarto")
    print("Lagarto come Papel")
    print("Papel refuta Spock")
    print("Spock vaporiza Pedra")
    print("Pedra esmaga Tesoura")
    print("")
def exibir_introducao():
    print("")
    print("Esse jogo é inspirado em uma versão do")
    print("Pedra, Papel e Tesoura criado pelo personagem")
    print("Dr. Sheldon Lee Cooper da série The Big Bang Theory")
    print("(minha série favorita desde que assisti pela primeira vez)")
    print("onde aqui temos dois personagens adicionais:")
    print("- Lagarto")
    print("- Spock")
    print("O personagem Spock é o famoso Spock da franquia Star Trek")
    print("(uma das minhas favoritas).")
    print()
    print("Divirta-se!")
    print()
    print("Vida Longa e Próspera!!")
    print("")
def obter_jogada():
    print("")
    escolha = input("Você escolheu: ")
    print("")
    while escolha not in ["1", "2", "3", "4", "5"]:
        print("Escolha inválida. Digite novamente.")
        escolha = input("Digite o número correspondente à sua jogada: ")
        print("")
    opcoes = ["pedra", "papel", "tesoura", "lagarto", "spock"]
    jogada = opcoes[int(escolha) - 1]
    return jogada

while True:
    exibir_menu_principal()

    opcao = input("Digite o número correspondente à opção desejada: ")

    if opcao == "1":
        print("Iniciando o jogo...")
        exibir_menu_principal()
        print("Digite o número correspondente à sua jogada")
        jogada1 = obter_jogada()

        jogada2 = random.choice(["pedra", "papel", "tesoura", "lagarto", "spock"])
        print("O Computador escolheu:", jogada2)
        print("")

        resultado = jogo_pedra_papel_tesoura_lagarto_spock(jogada1, jogada2)
        print(resultado)
        print("")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        print("")
        if jogar_novamente.lower() != "s":
            break
    elif opcao == "2":
        exibir_regras()
    elif opcao == "3":
        exibir_introducao()
    elif opcao == "4":
        print("Saindo do jogo...")
        break
    else:
        print("Opção inválida. Digite novamente.")

print("Obrigado por jogar!")
