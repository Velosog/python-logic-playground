"""
Ex04 — Analisador de Arquivo TXT

Objetivo:
Ler um arquivo .txt e gerar estatísticas:

- Número de linhas
- Número de palavras
- Número de caracteres
- Frequência das palavras (usando módulo de fundamentos)

Rodar:
python -m src.arquivos.analisador_txt
"""

from pathlib import Path
from src.fundamentos.listas_dicts import frequencia_palavras


def analisar_arquivo(caminho: Path) -> None:
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    texto = caminho.read_text(encoding="utf-8")

    linhas = texto.splitlines()
    palavras = texto.split()
    caracteres = len(texto)

    print("\n=== ESTATÍSTICAS DO ARQUIVO ===")
    print(f"Linhas: {len(linhas)}")
    print(f"Palavras: {len(palavras)}")
    print(f"Caracteres: {caracteres}")

    print("\n=== FREQUÊNCIA DE PALAVRAS ===")
    freq = frequencia_palavras(texto)

    for palavra, qtd in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{palavra}: {qtd}")


if __name__ == "__main__":
    base_dir = Path(__file__).parent
    arquivo = base_dir / "data" / "exemplo.txt"

    analisar_arquivo(arquivo)
