from operazioni import divisione
import pytest

# --- Test Divisione ---
def test_divisione_positivi():
    assert divisione(10, 2) == 5.0

def test_divisione_negativi():
    assert divisione(-10, -2) == 5.0

def test_divisione_mista():
    assert divisione(10, -2) == -5.0

def test_divisione_periodica():
    # Usiamo pytest.approx per i float con decimali infiniti
    assert divisione(10, 3) == pytest.approx(3.333333333)

def test_divisione_per_zero():
    assert divisione(10, 0) is None

def test_divisione_tipi_errati():
    assert divisione(10, "2") is None