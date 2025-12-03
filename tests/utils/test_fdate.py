from datetime import datetime, timedelta
from utils.fdate import fdate

def test_fecha_actual():
    expected = datetime.now().strftime("%Y-%m-%d")
    result = fdate("%Y-%m-%d")
    assert result == expected

def test_fecha_pasada():
    dias = -5
    expected = (datetime.now() + timedelta(days=dias)).strftime("%d/%m/%Y")
    result = fdate("%d/%m/%Y", dias)
    assert result == expected

def test_fecha_futura():
    dias = 3
    expected = (datetime.now() + timedelta(days=dias)).strftime("%Y%m%d")
    result = fdate("%Y%m%d", dias)
    assert result == expected