import pytest
import tempfile
from pathlib import Path
from macr.system import Layer, System
from macr.library import Pb, CsI
import numpy as np


@pytest.fixture
def sample_linear_system():
    system = System()
    system.add(Layer(Pb, 0.1, 0))
    system.add(Layer(Pb, 0.1, 0))
    system.add(Layer(CsI, 0.1, 1))
    system.add(Layer(Pb, 0.1, 0))
    system.add(Layer(CsI, 0.1, 1))
    return system


@pytest.fixture
def sample_layer():
    return Layer(Pb, 0.1, 0)


## Testing Layers
def test_layer_creation(sample_layer):
    assert sample_layer.material.materialstr == "Pb"
    assert sample_layer.thickness == 0.1
    assert sample_layer.active == 0


def test_layer_set_energies(sample_layer):
    original_energies = sample_layer.energies
    energies = np.linspace(1, 10, 10)
    assert len(sample_layer.energies) != len(energies)
    sample_layer.set_energies(energies)
    assert all(sample_layer.energies == energies)
    sample_layer.set_energies(original_energies)


def test_layer_set_engine(sample_layer):
    nist_cross_section = sample_layer.material.sigma[0]
    assert sample_layer.material.engine.name == "NIST", (
        "Engine didn't initialise as expected"
    )
    sample_layer.set_engine("SRIM")
    assert sample_layer.material.engine.name == "SRIM", (
        "Engine didn't switch as expected"
    )
    srim_cross_section = sample_layer.material.sigma[0]
    assert nist_cross_section != srim_cross_section, (
        "Engine switch hasn't updated cross-sections"
    )
    sample_layer.set_engine("NIST")


def test_layer_get_transmission(sample_layer):
    """
    This test is horrendously fragile.
    changes to library.ENERGIES or .ENGINE would break it.
    """
    pre_defined_mean = 0.5616514735215689
    new_layer_mean = np.mean(sample_layer.get_transmission())

    assert np.isclose(
        new_layer_mean, pre_defined_mean
    ), """Transmission values no longer match, check if default engine has changed from
         NIST or default energies have changed from ENERGIES = np.geomspace(0.01, 1, 10000)"""


## Testing Systems
def test_system_saving_and_loading(sample_linear_system):
    """Test system can be saved and loaded with consistency check."""
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = Path(tmpdir) / "test_system.pk"

        # Save system
        sample_linear_system._saveSystem(str(filepath))
        assert filepath.exists(), "System file was not created"

        # Load system into new variable
        loaded_system = System()
        loaded_system._loadSystem(str(filepath))

        # Check consistency
        assert len(sample_linear_system) == len(loaded_system), (
            "System lengths don't match"
        )

        for i in range(len(sample_linear_system)):
            assert sample_linear_system[i].thickness == loaded_system[i].thickness, (
                f"Layer {i} thickness mismatch"
            )
            assert sample_linear_system[i].active == loaded_system[i].active, (
                f"Layer {i} active flag mismatch"
            )


def test_system_dataframe_after_loading(sample_linear_system):
    """Test that loaded system produces identical DataFrame."""
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = Path(tmpdir) / "test_system.pk"

        original_df = sample_linear_system.to_dataframe()

        sample_linear_system._saveSystem(str(filepath))
        loaded_system = System()
        loaded_system._loadSystem(str(filepath))
        loaded_df = loaded_system.to_dataframe()

        # Compare DataFrames
        assert original_df.equals(loaded_df), "DataFrames don't match after load"
