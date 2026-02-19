import pytest

from src.funcoes.ex02_dinheiro_br import parse_dinheiro_br


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ("R$ 1.234,56", 123456),
        ("1234,56", 123456),
        ("1.234", 123400),
        ("10", 1000),
        ("0,99", 99),
        ("R$0,5", 50),
        ("0", 0),
        (",50", 50),
        ("0001,20", 120),
    ],
)
def test_parse_dinheiro_br_validos(entrada, esperado):
    assert parse_dinheiro_br(entrada) == esperado


@pytest.mark.parametrize(
    "entrada",
    [
        "",                 # vazio
        "R$ ",              # vazio com prefixo
        "1,234",            # 3 decimais
        "1,2,3",            # múltiplas vírgulas
        "1.2.3,45",         # milhar zoado mas ainda passa chars -> vamos considerar inválido?
        "abc",              # letras
        "R$ -10,00",        # sinal não suportado no parser básico
        "10.00",            # decimal com ponto (não aceito no BR)
        "1..000",           # pontos duplicados
    ],
)
def test_parse_dinheiro_br_invalidos(entrada):
    with pytest.raises(ValueError):
        parse_dinheiro_br(entrada)


def test_parse_dinheiro_br_tipo_invalido():
    with pytest.raises(TypeError):
        parse_dinheiro_br(123)  # type: ignore[arg-type]
