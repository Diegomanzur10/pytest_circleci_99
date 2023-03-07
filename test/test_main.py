from code.main import suma, resta, multiplicacion, division
import pytest

@pytest.mark.parametrize(
        (
            "a",
            "b",
            "valor_esperado"
        ),
        [
            (
                3,
                4,
                7
            ),
            (
                10,
                2,
                12
            )
        ],
        ids=[
            "Test1",
            "Test2"
        ]
)
def test_suma(a, b, valor_esperado):
    assert suma(a, b) == valor_esperado

#@pytest.mark.skip(reason = "Funcion a depricar")
@pytest.mark.xfail()
def test_division():
    assert division(1, 0) == 1
