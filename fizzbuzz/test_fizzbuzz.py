import pytest
from fizzbuzz import fizz_buzz


def test_fizz_buzz():
    assert fizz_buzz(3) == 'Fizz'
    assert fizz_buzz(5) == 'Buzz'
    assert fizz_buzz(15) == 'FizzBuzz'
