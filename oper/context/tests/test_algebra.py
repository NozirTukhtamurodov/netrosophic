from ..types import NeutrosophicSet
from ...algebra import (
    AlgebraicSumOperation,
    AlgebraicProductOperation,
    ScalarMultiplicationOperation
)
from . import assert_with_round

def test_algebraic_sum_operation():
    op = AlgebraicSumOperation()
    n1 = NeutrosophicSet(0.7, 0.4, 0.2)
    n2 = NeutrosophicSet(0.5, 0.3, 0.1)
    result = op.operate(n1, n2)
    assert_with_round(result.truth, 0.85)
    assert_with_round(result.indeterminacy, 0.12)
    assert_with_round(result.falsity, 0.28)

def test_algebraic_product_operation():
    op = AlgebraicProductOperation()
    n1 = NeutrosophicSet(0.6, 0.5, 0.3)
    n2 = NeutrosophicSet(0.7, 0.4, 0.2)
    result = op.operate(n1, n2)
    assert_with_round(result.truth, 0.42)
    assert_with_round(result.indeterminacy, 0.7)
    assert_with_round(result.falsity, 0.06)

def test_scalar_multiplication_operation():
    op = ScalarMultiplicationOperation()
    n = NeutrosophicSet(0.8, 0.4, 0.2)
    result = op.operate(n, 0.5)  # Scalar operation ignores the second operand
    assert_with_round(result.truth, 0.4)
    assert_with_round(result.indeterminacy, 0.2)
    assert_with_round(result.falsity, 0.1)
