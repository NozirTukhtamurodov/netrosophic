from ..types import NeutrosophicSet
from ..calculator import NeutrosophicCalculator
from ...arithmetic import AdditionOperation
from ...algebra import AlgebraicSumOperation
from . import assert_with_round


def test_neutrosophic_calculator_with_arithmetic_operation():
    calculator = NeutrosophicCalculator(AdditionOperation())
    n1 = NeutrosophicSet(0.6, 0.3, 0.2)
    n2 = NeutrosophicSet(0.4, 0.2, 0.1)
    result = calculator.calculate(n1, n2)
    assert_with_round(result.truth, 1.0)
    assert_with_round(result.indeterminacy, 0.5)
    assert_with_round(result.falsity, 0.3)


def test_neutrosophic_calculator_with_algebraic_operation():
    calculator = NeutrosophicCalculator(AlgebraicSumOperation())
    n1 = NeutrosophicSet(0.7, 0.5, 0.3)
    n2 = NeutrosophicSet(0.6, 0.4, 0.2)
    result = calculator.calculate(n1, n2)
    assert_with_round(result.truth, 0.88)
    assert_with_round(result.indeterminacy, 0.2)
    assert_with_round(result.falsity, 0.44)
