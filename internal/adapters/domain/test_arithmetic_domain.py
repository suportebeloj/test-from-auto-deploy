

from internal.adapters.domain.arithmetic import ArithCore


def test_calc_sum():
    mockData = [(1,2,3), (3,3,6), (2,2,4)]

    core = ArithCore()
    for v in mockData:
        assert core.addition(v[0], v[1]) == v[2]


def test_calc_sub():
    mockData = [(1,2,-1), (3,3,0), (2,2,0), (10,3,7)]

    core = ArithCore()
    for v in mockData:
        assert core.subtraction(v[0], v[1]) == v[2]

def test_calc_mult():
    mockData = [(1,2,2), (3,3,9), (2,2,4), (10,3,30)]

    core = ArithCore()
    for v in mockData:
        assert core.multiplication(v[0], v[1]) == v[2]
