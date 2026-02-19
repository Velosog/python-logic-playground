"""
Ex01 — Normalizador de texto

Objetivo:
Criar uma função que "limpa" texto para uso em sistemas reais:
- remove espaços extras
- converte para minúsculo
- remove pontuação (opcional)
- mantém apenas letras/números/espaços (opcional)

Rodar:
python src/funcoes/ex01_normalizador.py
"""

from __future__ import annotations

import re


def normalizar_texto(
    texto: str,
    *,
    lower: bool = True,
    remover_pontuacao: bool = True,
    compactar_espacos: bool = True,
) -> str:
    """
    Normaliza um texto para comparações, buscas e armazenamento.

    Args:
        texto: string de entrada
        lower: se True, converte para minúsculo
        remover_pontuacao: se True, remove pontuação e símbolos
        compactar_espacos: se True, transforma múltiplos espaços em 1

    Returns:
        Texto normalizado.
    """
    if not isinstance(texto, str):
        raise TypeError("texto deve ser str")

    resultado = texto.strip()

    if lower:
        resultado = resultado.lower()

    if remover_pontuacao:
        # Mantém letras/números/espaços. Remove símbolos e pontuação.
        resultado = re.sub(r"[^\w\s]", "", resultado, flags=re.UNICODE)

    if compactar_espacos:
        resultado = re.sub(r"\s+", " ", resultado).strip()

    return resultado


if __name__ == "__main__":
    exemplos = [
        "  Oi, Gabi!!!   ",
        "Python   é   FORTE.",
        "Duda & Lucas;  aula #1",
        "   texto   com     MUITO     espaço   ",
    ]

    for e in exemplos:
        print("IN :", repr(e))
        print("OUT:", repr(normalizar_texto(e)))
        print("-" * 40)
