import os
import pytest

# Carpetas y archivos que deben existir
REQUIRED_PATHS = [
    '.env',
    'config',
    'utils',
    'tests',
]

@pytest.mark.parametrize('path', REQUIRED_PATHS)
def test_required_paths_exist(path):
    abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', path))
    assert os.path.exists(abs_path), f"No se encuentra: {abs_path}"
