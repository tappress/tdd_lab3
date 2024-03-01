from typing import Optional


class Company:
    def __init__(self, parent: Optional["Company"] = None, employee_count: int = 0):
        self._validate_parent(parent)
        self._validate_employee_count(employee_count)

        self._parent = parent
        self._employee_count = employee_count

    @staticmethod
    def _validate_employee_count(value: int) -> None:
        if type(value) is not int:
            raise TypeError("Employee count must be an integer.")

        if value < 0:
            raise ValueError("Employee count must be greater than 0.")

    def _validate_parent(self, parent: Optional["Company"]):
        if parent is self:
            raise ValueError("Company cannot be parent to itself")

    @property
    def parent(self) -> Optional["Company"]:
        return self._parent

    @parent.setter
    def parent(self, parent: Optional["Company"]):
        self._validate_parent(parent)
        self._parent = parent

    @property
    def employee_count(self) -> int:
        return self._employee_count

    @employee_count.setter
    def employee_count(self, employee_count: int):
        self._validate_employee_count(employee_count)
        self._employee_count = employee_count

    def __repr__(self) -> str:
        return f"Company(parent={self._parent}, employee_count={self.employee_count})"
