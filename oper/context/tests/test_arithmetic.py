from ..types import NeutrosophicSet
from ...arithmetic import (
    AdditionOperation,
    SubtractionOperation,
    MultiplicationOperation,
    DivisionOperation
)
from . import assert_with_round


def test_addition_operation():
    op = AdditionOperation()
    n1 = NeutrosophicSet(0.6, 0.3, 0.2)
    n2 = NeutrosophicSet(0.4, 0.2, 0.1)
    result = op.operate(n1, n2)
    assert_with_round(result.truth, 1.0)
    assert_with_round(result.indeterminacy, 0.5)
    assert_with_round(result.falsity, 0.3)

def test_subtraction_operation():
    op = SubtractionOperation()
    n1 = NeutrosophicSet(0.7, 0.4, 0.2)
    n2 = NeutrosophicSet(0.3, 0.2, 0.1)
    result = op.operate(n1, n2)
    assert_with_round(result.truth, 0.4)
    assert_with_round(result.indeterminacy, 0.2)
    assert_with_round(result.falsity, 0.1)

def test_multiplication_operation():
    op = MultiplicationOperation()
    n1 = NeutrosophicSet(0.8, 0.5, 0.2)
    n2 = NeutrosophicSet(0.6, 0.4, 0.3)
    result = op.operate(n1, n2)
    assert_with_round(result.truth, 0.48)
    assert_with_round(result.indeterminacy, 0.2)
    assert_with_round(result.falsity, 0.06)

def test_division_operation():
    op = DivisionOperation()
    n1 = NeutrosophicSet(0.8, 0.5, 0.2)
    n2 = NeutrosophicSet(0.4, 0.3, 0.1)
    result = op.operate(n1, n2)
    assert_with_round(result.truth, 1.0)
    assert_with_round(result.indeterminacy, 1.0)
    assert_with_round(result.falsity, 1.0)
