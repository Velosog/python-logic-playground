"""
Módulo: listas_dicts

Objetivo:
Revisar e praticar operações com listas e dicionários em Python.
"""

from typing import List, Dict


def contar_pares(numeros: List[int]) -> int:
    """
    Retorna a quantidade de números pares em uma lista.
    """
    return sum(1 for n in numeros if n % 2 == 0)


def tamanho_dos_nomes(nomes: List[str]) -> Dict[str, int]:
    """
    Retorna um dicionário com o nome e o tamanho de cada string.
    """
    return {nome: len(nome) for nome in nomes}


import re


def frequencia_palavras(texto: str) -> Dict[str, int]:
    """
    Conta a frequência de cada palavra em um texto,
    ignorando pontuação e diferenças de maiúsculas/minúsculas.
    """
    palavras = re.findall(r"\b\w+\b", texto.lower())
    frequencia: Dict[str, int] = {}

    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1

    return frequencia


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6]
    nomes = ["Gabi", "Duda", "Lucas"]
    texto = "python é bom python é forte"

    print("Quantidade de pares:", contar_pares(numeros))
    print("Tamanho dos nomes:", tamanho_dos_nomes(nomes))
    print("Frequência de palavras:", frequencia_palavras(texto))
