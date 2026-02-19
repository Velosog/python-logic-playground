"""
CLI — Interface de linha de comando

Integra:
- normalizador de texto
- parser de dinheiro BR

Rodar:
python src/controle/cli.py
"""

from src.funcoes.ex01_normalizador import normalizar_texto
from src.funcoes.ex02_dinheiro_br import parse_dinheiro_br


def menu() -> None:
    while True:
        print("\n=== PYTHON LOGIC PLAYGROUND ===")
        print("1 - Converter dinheiro BR para centavos")
        print("2 - Normalizar texto")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            converter_dinheiro()
        elif escolha == "2":
            normalizar()
        elif escolha == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


def converter_dinheiro() -> None:
    valor = input("Digite um valor em formato BR: ")

    try:
        centavos = parse_dinheiro_br(valor)
        print(f"Resultado: {centavos} centavos")
    except Exception as e:
        print(f"Erro: {e}")


def normalizar() -> None:
    texto = input("Digite um texto: ")

    try:
        resultado = normalizar_texto(texto)
        print(f"Normalizado: {resultado}")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    menu()
