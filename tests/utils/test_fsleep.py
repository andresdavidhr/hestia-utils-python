import os
import sys
from utils.fsleep import fsleep

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

def test_fsleep_runs():
    try:
        fsleep(1)
    except Exception as e:
        assert False, f"fsleep lanzó una excepción: {e}"
