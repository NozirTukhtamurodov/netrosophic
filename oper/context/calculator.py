from typing import Union
from .types import NeutrosophicSet
from ..arithmetic import AdditionOperation, SubtractionOperation, MultiplicationOperation, DivisionOperation
from ..algebra import ScalarMultiplicationOperation


class NeutrosophicCalculator:
    def __init__(self, operation: AdditionOperation | SubtractionOperation | MultiplicationOperation | DivisionOperation):
        self.operation = operation

    def set_operation(self, operation):
        self.operation = operation

    def calculate(self, a: NeutrosophicSet, b: Union[NeutrosophicSet, float]) -> NeutrosophicSet:
        if isinstance(b, NeutrosophicSet):
            return self.operation.operate(a, b)
        elif isinstance(b, float):
            return ScalarMultiplicationOperation().operate(a, b)
        else:
            raise TypeError("Unsupported type for operation.")
