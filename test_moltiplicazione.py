from operazioni import moltiplicazione
import pytest

# --- Test Moltiplicazione ---
def test_moltiplicazione_positivi():
    assert moltiplicazione(3, 4) == 12

def test_moltiplicazione_negativi():
    assert moltiplicazione(-2, -5) == 10

def test_moltiplicazione_zero():
    assert moltiplicazione(5, 0) == 0

def test_moltiplicazione_float():
    assert moltiplicazione(2.5, 2) == 5.0

def test_moltiplicazione_tipi_errati():
    assert moltiplicazione("3", 4) is None