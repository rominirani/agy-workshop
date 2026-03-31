import math
from typing import List, Optional, Any

class Calculator:
    """A modular calculator to process and log mathematical operations."""

    def __init__(self):
        self.history: List[str] = []

    def _log_operation(self, op_type: str, args: tuple, result: Any) -> None:
        """Internal helper to log operation details."""
        entry = f"Type: {op_type}, Args: {args}, Result: {result}"
        self.history.append(entry)
        print(f"PROCESSED: {entry}")

    def add(self, a: float, b: float) -> float:
        res = a + b
        self._log_operation("ADD", (a, b), res)
        return res

    def multiply(self, a: float, b: float) -> float:
        res = a * b
        self._log_operation("MUL", (a, b), res)
        return res

    def divide(self, a: float, b: float) -> Optional[float]:
        if b == 0:
            print("ERROR: DIVISION BY ZERO")
            self._log_operation("DIV", (a, b), "ERROR")
            return None
        res = a / b
        self._log_operation("DIV", (a, b), res)
        return res

    def power(self, a: float, b: float) -> float:
        res = math.pow(a, b)
        self._log_operation("POW", (a, b), res)
        return res

    def square_root(self, a: float) -> Optional[float]:
        if a < 0:
            print("ERROR: NEGATIVE SQRT")
            self._log_operation("SQRT", (a,), "ERROR")
            return None
        res = math.sqrt(a)
        self._log_operation("SQRT", (a,), res)
        return res

    def print_history(self):
        print("\n--- OPERATION HISTORY ---")
        for i, entry in enumerate(self.history):
            print(f"{i}: {entry}")

if __name__ == "__main__":
    calc = Calculator()
    calc.add(10, 20)
    calc.multiply(5, 4)
    calc.divide(10, 0)
    calc.print_history()
