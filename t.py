from typing import Tuple

class NeutrosophicSet:
    def __init__(self, truth: float, indeterminacy: float, falsity: float) -> None:
        self.truth = self._clamp(truth)
        self.indeterminacy = self._clamp(indeterminacy)
        self.falsity = self._clamp(falsity)

    def _clamp(self, value: float) -> float:
        """Clamp the value to the range [0, 1]."""
        return max(0.0, min(1.0, value))

    def algebraic_sum(self, other: "NeutrosophicSet") -> "NeutrosophicSet":
        """Perform the algebraic sum operation on two neutrosophic sets."""
        truth_sum = self.truth + other.truth - self.truth * other.truth
        indeterminacy_sum = self.indeterminacy + other.indeterminacy - self.indeterminacy * other.indeterminacy
        falsity_sum = self.falsity + other.falsity - self.falsity * other.falsity

        return NeutrosophicSet(
            truth=self._clamp(truth_sum),
            indeterminacy=self._clamp(indeterminacy_sum),
            falsity=self._clamp(falsity_sum)
        )

    def __repr__(self) -> str:
        return (f"NeutrosophicSet(T={self.truth:.2f}, "
                f"I={self.indeterminacy:.2f}, F={self.falsity:.2f})")

# Example usage
if __name__ == "__main__":
    set_a = NeutrosophicSet(0.9, 0.8, 0.7)
    set_b = NeutrosophicSet(0.6, 0.5, 0.9)

    result = set_a.algebraic_sum(set_b)
    print(f"Algebraic sum of Set A and Set B: {result}")
