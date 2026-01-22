from operazioni import sottrazione


def test_sottrazione_positivi():
    assert sottrazione(10, 5) == 5

def test_sottrazione_negativi():
    assert sottrazione(-5, -3) == -2

def test_sottrazione_misti():
    assert sottrazione(-2, 3) == -5
    assert sottrazione(10, -5) == 15

def test_sottrazione_float():
    assert sottrazione(10.5, 0.5) == 10.0

def test_sottrazione_float_misti():
    assert sottrazione(5.5, -2.5) == 8.0

def test_sottrazione_zero():
    assert sottrazione(0, 0) == 0
    assert sottrazione(5, 0) == 5

def test_sottrazione_con_stringa():
    assert sottrazione("10", 5) is None

def test_sottrazione_con_none():
    assert sottrazione(None, 5) is None

def test_sottrazione_con_lista():
    assert sottrazione([10], 5) is None

def test_sottrazione_con_booleani():
    # In Python True = 1 e False = 0
    assert sottrazione(True, False) == 1
    assert sottrazione(5, True) == 4
