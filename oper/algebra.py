from .context.types import NeutrosophicSet


class AlgebraicSumOperation:
    def operate(self, a: NeutrosophicSet, b: NeutrosophicSet) -> NeutrosophicSet:
        return NeutrosophicSet(
            a.truth + b.truth - a.truth * b.truth,
            a.indeterminacy * b.indeterminacy,
            a.falsity + b.falsity - a.falsity * b.falsity
        )

class AlgebraicProductOperation:
    def operate(self, a: NeutrosophicSet, b: NeutrosophicSet) -> NeutrosophicSet:
        return NeutrosophicSet(
            a.truth * b.truth,
            a.indeterminacy + b.indeterminacy - a.indeterminacy * b.indeterminacy,
            a.falsity * b.falsity
        )

class ScalarMultiplicationOperation:
    def operate(self, a: NeutrosophicSet, scalar: float) -> NeutrosophicSet:
        if not (0 <= scalar <= 1):
            raise ValueError("Scalar must be in the range [0, 1].")

        return NeutrosophicSet(
            a.truth * scalar,
            a.indeterminacy * scalar,
            a.falsity * scalar
        )
