from utils.fsleep import fsleep

def test_fsleep_runs():
    try:
        fsleep(1)
    except Exception as e:
        assert False, f"fsleep lanzó una excepción: {e}"
