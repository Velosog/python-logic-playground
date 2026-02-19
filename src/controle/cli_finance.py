"""
Ex07 — CLI Financeiro

Integra:
- JSON (db_json)
- Parser dinheiro BR
- Normalizador de texto

Rodar:
python -m src.controle.cli_finance
"""

from collections import defaultdict

from src.arquivos.db_json import (
    adicionar_registro,
    listar_registros,
    remover_por_id,
    carregar_db,
)


def resumo_por_categoria() -> None:
    dados = carregar_db()

    if not dados:
        print("Banco vazio.")
        return

    totais = defaultdict(int)

    for r in dados:
        totais[r["categoria"]] += r["valor_centavos"]

    print("\n=== RESUMO POR CATEGORIA ===")
    for cat, total in sorted(totais.items(), key=lambda x: x[1], reverse=True):
        reais = total // 100
        centavos = total % 100
        print(f"{cat}: R$ {reais},{centavos:02d}")


def menu() -> None:
    while True:
        print("\n=== FINANCE CLI ===")
        print("1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Resumo por categoria")
        print("4 - Remover por ID")
        print("5 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            categoria = input("Categoria: ")
            descricao = input("Descrição: ")
            valor = input("Valor (BR): ")
            try:
                adicionar_registro(categoria, descricao, valor)
            except Exception as e:
                print("Erro:", e)

        elif opcao == "2":
            listar_registros()

        elif opcao == "3":
            resumo_por_categoria()

        elif opcao == "4":
            rid = input("ID do registro: ")
            remover_por_id(rid)

        elif opcao == "5":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
