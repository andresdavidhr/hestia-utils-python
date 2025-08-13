from utils.fuuid4 import fnc_generar_uuid4
import uuid

def test_fnc_generar_uuid4_returns_valid_uuid():
    result = fnc_generar_uuid4()
    try:
        val = uuid.UUID(result, version=4)
    except ValueError:
        assert False, f"Returned value is not a valid UUID4: {result}"
    assert val.version == 4
