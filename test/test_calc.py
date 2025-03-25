from src.calc import Calculator

calc = Calculator()

def test_multiply ():
    assert calc.multiply(1,1) == 1
    assert calc.multiply(2,2) == 4
    assert calc.multiply(3,3) == 9
    assert calc.multiply(10,-10) == -100
    assert calc.multiply(5,5) == 25
    assert calc.multiply(10,5) == 50

def test_divide ():
    assert calc.divide(12,2) == 6
    assert calc.divide(10,10) == 1
    assert calc.divide(25,5) == 5
    assert calc.divide(100,1) == 100
    assert calc.divide(10.9,5) == 2.18
    