import unittest
from utils.fuuid4 import fnc_generar_uuid4
import uuid

class TestFuuid4(unittest.TestCase):
    def test_fnc_generar_uuid4_returns_valid_uuid(self):
        result = fnc_generar_uuid4()
        # Check if the result is a valid UUID4
        try:
            val = uuid.UUID(result, version=4)
        except ValueError:
            self.fail(f"Returned value is not a valid UUID4: {result}")
        self.assertEqual(val.version, 4)

if __name__ == "__main__":
    unittest.main()
