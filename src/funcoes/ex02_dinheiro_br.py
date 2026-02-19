"""
Ex02 — Parser de dinheiro BR

Objetivo:
Converter strings comuns do Brasil para centavos (int), com validação.

Exemplos aceitos:
- "R$ 1.234,56"
- "1234,56"
- "1.234"
- "10"
- "0,99"

Saída:
- retorna int em centavos (ex: "1.234,56" -> 123456)

Rodar:
python src/funcoes/ex02_dinheiro_br.py
"""

from __future__ import annotations

import re

def parse_dinheiro_br(valor: str) -> int:
    if not isinstance(valor, str):
        raise TypeError("valor deve ser str")

    s = valor.strip()
    s = re.sub(r"^\s*R\$\s*", "", s)
    s = s.replace(" ", "")

    if s == "":
        raise ValueError("valor vazio")
    
    # aceita ",50" como "0,50"
    if s.startswith(","):
        s = "0" + s

    # Regex rigorosa formato BR:
    # - parte inteira: 1-3 dígitos seguidos de grupos opcionais .xxx
    # - decimal opcional com ,xx
    padrao = r"^\d{1,3}(?:\.\d{3})*(?:,\d{1,2})?$|^\d+(?:,\d{1,2})?$"

    if not re.fullmatch(padrao, s):
        raise ValueError(f"formato inválido: {valor!r}")

    if "," in s:
        parte_int, parte_dec = s.split(",")
    else:
        parte_int, parte_dec = s, ""

    parte_int = parte_int.replace(".", "")

    if parte_dec == "":
        parte_dec = "00"
    elif len(parte_dec) == 1:
        parte_dec += "0"

    return int(parte_int) * 100 + int(parte_dec)

if __name__ == "__main__":
    exemplos = [
        "R$ 1.234,56",
        "1234,56",
        "1.234",
        "10",
        "0,99",
        "R$0,5",
    ]

    for e in exemplos:
        centavos = parse_dinheiro_br(e)
        print(f"{e!r} -> {centavos} centavos")
