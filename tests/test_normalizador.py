import pytest

from src.funcoes.ex01_normalizador import normalizar_texto


def test_normalizar_texto_basico():
    assert normalizar_texto("  Oi, Gabi!!!   ") == "oi gabi"


def test_normalizar_texto_sem_lower():
    assert normalizar_texto("Oi, Gabi!", lower=False) == "Oi Gabi"


def test_normalizar_texto_sem_remover_pontuacao():
    assert normalizar_texto("Oi, Gabi!", remover_pontuacao=False) == "oi, gabi!"


def test_normalizar_texto_compacta_espacos():
    assert normalizar_texto("  a   b    c  ") == "a b c"


def test_normalizar_texto_tipo_invalido():
    with pytest.raises(TypeError):
        normalizar_texto(123)  # type: ignore[arg-type]
