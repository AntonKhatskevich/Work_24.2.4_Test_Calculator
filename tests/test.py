import pytest

from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 78, 90) == 168

    def test_division_success(self):
        assert self.calc.division(self, 50, 25) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(self, 52, 20) == 1040

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 156, 129) == 27
