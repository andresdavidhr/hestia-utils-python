import unittest
from utils.fsleep import fsleep

class TestFSleep(unittest.TestCase):
    def test_fsleep_runs(self):
        # Solo comprobamos que no lanza excepción
        try:
            fsleep(1)
        except Exception as e:
            self.fail(f"fsleep lanzó una excepción: {e}")

if __name__ == "__main__":
    unittest.main()
