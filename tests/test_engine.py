import pytest
from macr.engine import Engine
import pandas as pd


@pytest.fixture
def engine_names():
    return ["NIST", "ESTAR", "PSTAR", "SRIM"]


@pytest.fixture
def init_nist_engine(engine_names):
    return Engine(engine_names[0])


@pytest.fixture
def init_estar_engine(engine_names):
    return Engine(engine_names[1])


@pytest.fixture
def init_pstar_engine(engine_names):
    return Engine(engine_names[2])


@pytest.fixture
def init_srim_engine(engine_names):
    return Engine(engine_names[3])


### Initialisation testing
def test_fail_on_wrong_engine_name():
    with pytest.raises(AssertionError):
        Engine("fake_engine")


def test_engine_name(engine_names):
    for name in engine_names:
        init_engine = Engine(name)
        assert init_engine.name == name


def test_engine_db_initilisation(init_nist_engine):
    assert isinstance(init_nist_engine.db, dict)


def test_atomic_db_creation(init_nist_engine):
    assert isinstance(init_nist_engine.db["atomic"], pd.DataFrame)
    assert all(
        col in init_nist_engine.db["atomic"].columns
        for col in ["Z", "Symbol", "Name", "Weight", "Density"]
    )


## Engine Specific Testing - Nist
def test_nist_material_list_generation(init_nist_engine):
    assert len(init_nist_engine._generate_material_list()) == 100


def test_nist_missing_atomic_entries(init_nist_engine):
    assert init_nist_engine.missing_atomic_entries() == []


## Engine Specific Testing - SRIM
def test_srim_material_list_generation(init_srim_engine):
    assert len(init_srim_engine._generate_material_list()) == 92


def test_srim_missing_atomic_entries(init_srim_engine):
    assert init_srim_engine.missing_atomic_entries() == [
        "Am",
        "Bk",
        "Cf",
        "Cm",
        "Es",
        "Fm",
        "Np",
        "Pu",
    ]
