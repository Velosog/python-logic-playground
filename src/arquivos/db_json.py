"""
Ex06 — Mini banco em JSON

Permite:
- adicionar registro
- listar registros
- remover registro por id

Rodar:
python -m src.arquivos.db_json
"""

from __future__ import annotations

import json
import uuid
from pathlib import Path
from datetime import datetime

from src.funcoes.ex02_dinheiro_br import parse_dinheiro_br
from src.funcoes.ex01_normalizador import normalizar_texto


DB_PATH = Path(__file__).parent / "data" / "db.json"


def carregar_db() -> list[dict]:
    if not DB_PATH.exists():
        return []

    with DB_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def salvar_db(dados: list[dict]) -> None:
    with DB_PATH.open("w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)


def adicionar_registro(categoria: str, descricao: str, valor_str: str) -> None:
    dados = carregar_db()

    registro = {
        "id": str(uuid.uuid4()),
        "data": datetime.now().strftime("%Y-%m-%d"),
        "categoria": normalizar_texto(categoria),
        "descricao": normalizar_texto(descricao),
        "valor_centavos": parse_dinheiro_br(valor_str),
    }

    dados.append(registro)
    salvar_db(dados)

    print("Registro adicionado com sucesso.")


def listar_registros() -> None:
    dados = carregar_db()

    if not dados:
        print("Banco vazio.")
        return

    for r in dados:
        print(r)


def remover_por_id(registro_id: str) -> None:
    dados = carregar_db()
    novos = [r for r in dados if r["id"] != registro_id]

    if len(novos) == len(dados):
        print("ID não encontrado.")
        return

    salvar_db(novos)
    print("Registro removido.")


if __name__ == "__main__":
    print("1 - Adicionar registro")
    print("2 - Listar registros")
    print("3 - Remover por ID")
    opcao = input("Escolha: ")

    if opcao == "1":
        cat = input("Categoria: ")
        desc = input("Descrição: ")
        val = input("Valor (BR): ")
        adicionar_registro(cat, desc, val)

    elif opcao == "2":
        listar_registros()

    elif opcao == "3":
        rid = input("ID do registro: ")
        remover_por_id(rid)

    else:
        print("Opção inválida.")
