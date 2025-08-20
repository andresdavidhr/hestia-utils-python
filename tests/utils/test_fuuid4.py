import os
import sys
from utils.fuuid4 import fnc_generar_uuid4
import uuid

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

def test_fnc_generar_uuid4_returns_valid_uuid():
    result = fnc_generar_uuid4()
    try:
        val = uuid.UUID(result, version=4)
    except ValueError:
        assert False, f"Returned value is not a valid UUID4: {result}"
    assert val.version == 4
