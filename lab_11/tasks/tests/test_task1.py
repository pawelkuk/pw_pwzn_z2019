import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)

test_run_data = [
    ("+", 1, 2, 3),
    ("-", 1, 2, -1),
    ("*", 1, -2, -2),
    ("/", 1, -2, -0.5),
]

test_run__invalid_data = [
    ("^", 1, 2, WrongOperation),
    ("-", "foo", 2, NotNumberArgument),
    ("*", 1, "bar", NotNumberArgument),
    ("/", 1, 0, CalculatorError),
    ("/", 1, 0.0, CalculatorError),
    ("/", 2, None, EmptyMemory),
]


@pytest.fixture(scope="function")
def calculator():
    print("\nNew calculator...")
    return Calculator()


@pytest.mark.parametrize("operator,arg1,arg2,expected", test_run_data)
def test_run_valid_operations(operator, arg1, arg2, expected, calculator):
    result = calculator.run(operator, arg1, arg2)
    assert result == expected


@pytest.mark.parametrize("operator,arg1,arg2,expected", test_run__invalid_data)
def test_run_invalid_data_raises_exceptions(operator, arg1, arg2, expected, calculator):
    with pytest.raises(expected):
        calculator.run(operator, arg1, arg2)


def test_memory_functionality(calculator: "Calculator"):
    calculator.run("+", 1, 2)
    assert calculator._short_memory == 3
    calculator.memorize()
    assert calculator.memory == 3
    calculator.clean_memory()
    with pytest.raises(EmptyMemory):
        calculator.in_memory()
    with pytest.raises(EmptyMemory):
        calculator.memory
