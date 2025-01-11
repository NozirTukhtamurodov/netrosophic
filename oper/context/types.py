

class NeutrosophicSet:
    def __init__(self, truth: float, indeterminacy: float, falsity: float):
        self.truth: float = self._clamp(truth)
        self.indeterminacy: float = self._clamp(indeterminacy)
        self.falsity: float = self._clamp(falsity)

    def __repr__(self) -> str:
        return f"NeutrosophicSet(T={self.truth}, I={self.indeterminacy}, F={self.falsity})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NeutrosophicSet):
            return NotImplemented

        return (
            self.truth == other.truth and
            self.indeterminacy == other.indeterminacy and
            self.falsity == other.falsity
        )

    def _clamp(self, value: float) -> float:
        """Clamp the value to the range [0, 1]."""
        return max(0.0, min(1.0, value))
