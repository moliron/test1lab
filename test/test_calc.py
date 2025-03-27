from src.calc import Calculator
import pytest
calc = Calculator()
@pytest.mark.parametrize(
        "a,b,expected",
        [
            (2,2,4),
            (-2,-5,10),
            (-2,-2,4),
            (-5,5.4,-27),
            (4,4,16)
        ]
)
def test_multiply (a,b,expected):
    assert calc.multiply(a,b) == expected 

@pytest.mark.parametrize(
        "v,g,expectedd",
        [
            (2,2,1),
            (3,3,1),
            (4,2,2),
            (10,5,2),
            (20,2,10)
        ]
)
def test_divide (v,g,expectedd):
    assert calc.divide(v,g) == expectedd

@pytest.mark.parametrize(
        "h,p,expecte",
        [
            (2,3,5),
            (3,3,6),
            (2,2,4),
            (12,23,35),
            (20,20,40)
        ]
)
def test_sum (h,p,expecte):
    assert calc.sum(h,p) == expecte


@pytest.mark.parametrize(
        "s,r,expect",
        [
            (100,10,90),
            (3,3,0),
            (12,2,10),
            (10,5,5),
            (20,20,0)
        ]
)
def test_subtract (s,r,expect):
    assert calc.subtract(s,r) == expect