import pytest
from calculadora import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    exponenciar,
    raiz_quadrada
)

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ]
)
def test_somar(a, b, esperado):
    assert somar(a, b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (10, 5, 5),
        (0, 0, 0),
        (-5, -5, 0),
    ]
)
def test_subtrair(a, b, esperado):
    assert subtrair(a, b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (4, 5, 20),
        (0, 100, 0),
        (-3, 3, -9),
    ]
)
def test_multiplicar(a, b, esperado):
    assert multiplicar(a, b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (10, 2, 5),
        (-10, 2, -5),
        (0, 5, 0),
        (10, 0, "Erro: divisão por zero."),
    ]
)
def test_dividir(a, b, esperado):
    assert dividir(a, b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (2, 3, 8),
        (5, 0, 1),
        (2, -1, 0.5),
    ]
)
def test_exponenciar(a, b, esperado):
    assert exponenciar(a, b) == esperado


@pytest.mark.parametrize(
    "a, esperado",
    [
        (9, 3),
        (0, 0),
        (-4, "Erro: número negativo não possui raiz quadrada real."),
    ]
)
def test_raiz_quadrada(a, esperado):
    assert raiz_quadrada(a) == esperado
