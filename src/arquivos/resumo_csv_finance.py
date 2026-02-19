"""
Ex05 — Resumo financeiro a partir de CSV

Lê um CSV com colunas:
data,categoria,descricao,valor

Gera:
- total geral (centavos)
- total por categoria (ranking)

Rodar:
python -m src.arquivos.resumo_csv_finance
"""

from __future__ import annotations

import csv
from pathlib import Path

from src.funcoes.ex02_dinheiro_br import parse_dinheiro_br


def ler_movimentacoes_csv(caminho: Path) -> list[dict]:
    if not caminho.exists():
        raise FileNotFoundError(f"CSV não encontrado: {caminho}")

    with caminho.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        linhas = list(reader)

    # valida colunas mínimas
    obrigatorias = {"data", "categoria", "descricao", "valor"}
    if not reader.fieldnames or not obrigatorias.issubset(set(reader.fieldnames)):
        raise ValueError(f"CSV precisa ter colunas: {sorted(obrigatorias)}")

    return linhas


def resumir_por_categoria(linhas: list[dict]) -> tuple[int, dict[str, int]]:
    total_geral = 0
    por_categoria: dict[str, int] = {}

    for row in linhas:
        categoria = (row.get("categoria") or "").strip()
        valor_str = (row.get("valor") or "").strip()

        if not categoria:
            raise ValueError("Linha com categoria vazia.")
        if not valor_str:
            raise ValueError("Linha com valor vazio.")

        centavos = parse_dinheiro_br(valor_str)

        total_geral += centavos
        por_categoria[categoria] = por_categoria.get(categoria, 0) + centavos

    return total_geral, por_categoria


def formatar_brl(centavos: int) -> str:
    sinal = "-" if centavos < 0 else ""
    centavos = abs(centavos)
    reais = centavos // 100
    cents = centavos % 100
    # separador de milhar com ponto
    reais_str = f"{reais:,}".replace(",", ".")
    return f"{sinal}R$ {reais_str},{cents:02d}"


if __name__ == "__main__":
    base = Path(__file__).parent
    csv_path = base / "data" / "exemplo.csv"

    linhas = ler_movimentacoes_csv(csv_path)
    total_geral, por_categoria = resumir_por_categoria(linhas)

    print("\n=== RESUMO FINANCEIRO (CSV) ===")
    print("Arquivo:", csv_path.name)
    print("Total geral:", formatar_brl(total_geral))

    print("\n--- Por categoria (maior -> menor) ---")
    for cat, total_cat in sorted(por_categoria.items(), key=lambda x: x[1], reverse=True):
        print(f"{cat}: {formatar_brl(total_cat)}")
