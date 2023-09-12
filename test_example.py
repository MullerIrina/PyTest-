from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 5, 4) == 9

    def test_division_success(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 4, 5) == -1

    def test_multiply_success(self):
         assert self.calc.multiply(self, 4, 5) == 20

    def teardown(self):
        print('Выполнение метода Teardown')