import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)

@pytest.fixture()
def calculator(scope='module'):
    return Calculator()


test_parameter_ok = [
    ('+', '3', '5', 8),
    ('+', '9', '10', 19),
    ('+', '100', '299', 399),
    ('-', '10', '4', 6),
    ('-', '7', '9', -2),
    ('-', '0', '1', -1),
    ('*', '10', '4', 40),
    ('*', '20', '0.25', 5),
    ('*', '0', '2', 0),
    ('/', '10', '2', 5),
    ('/', '1', '5', 0.2),
    ('/', '4', '8', 0.5),

]

test_parameter_exception = [
    ('*', 20, None, EmptyMemory),
    ('/', 2, 0, CalculatorError),
    ('^', 1, 5, WrongOperation),
    (2, 2, 2, WrongOperation),
    ('*', 'kot', 10, NotNumberArgument),
    ('/', 6, 'pies', NotNumberArgument),
]


@pytest.mark.parametrize("operator, arg1, arg2, expected", test_parameter_ok)
def test_run_ok_parameter(operator, arg1, arg2, expected, calculator):
    counting_result = calculator.run(operator, arg1, arg2)
    assert counting_result == expected


@pytest.mark.parametrize("operator, arg1, arg2, exception", test_parameter_exception)
def test_run_exception_parameter(operator, arg1, arg2, exception, calculator):
    with pytest.raises(exception):
        calculator.run(operator, arg1, arg2)


def test_calculator_memory(calculator: Calculator):
    calculator.run('*', 3, 2)
    assert calculator._short_memory == 6
    calculator.memorize()
    assert calculator.memory == 6
    calculator.clean_memory()
    with pytest.raises(EmptyMemory):
        calculator.memory()
    with pytest.raises(EmptyMemory):
        calculator.in_memory()
    calculator.run('+', 2, 2)
    assert calculator._short_memory == 4
