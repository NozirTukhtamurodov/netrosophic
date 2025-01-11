from .context.types import NeutrosophicSet


class AdditionOperation:
    def operate(self, a: NeutrosophicSet, b: NeutrosophicSet) -> NeutrosophicSet:
        return NeutrosophicSet(
            a.truth + b.truth,
            a.indeterminacy + b.indeterminacy,
            a.falsity + b.falsity,
        )

class SubtractionOperation:
    def operate(self, a: NeutrosophicSet, b: NeutrosophicSet) -> NeutrosophicSet:
        return NeutrosophicSet(
            a.truth - b.truth,
            a.indeterminacy - b.indeterminacy,
            a.falsity - b.falsity,
        )

class MultiplicationOperation:
    def operate(self, a: NeutrosophicSet, b: NeutrosophicSet) -> NeutrosophicSet:
        return NeutrosophicSet(
            a.truth * b.truth,
            a.indeterminacy * b.indeterminacy,
            a.falsity * b.falsity
        )

class DivisionOperation:
    def operate(self, a: NeutrosophicSet, b: NeutrosophicSet) -> NeutrosophicSet:
        if b.truth == 0 or b.indeterminacy == 0 or b.falsity == 0:
            raise ZeroDivisionError("Cannot divide by a neutrosophic number with zero in any component.")

        return NeutrosophicSet(
            a.truth / b.truth,
            a.indeterminacy / b.indeterminacy,
            a.falsity / b.falsity
        )
