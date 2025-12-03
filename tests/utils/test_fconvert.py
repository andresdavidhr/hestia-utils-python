from utils.fconvert import convert_crlf_to_lf

def test_convert_crlf_to_lf(tmp_path):
    # Crear archivo con CRLF
    file_path = tmp_path / "test_crlf.txt"
    file_path.write_bytes(b"linea1\r\nlinea2\r\nlinea3\r\n")
    # Ejecutar conversión
    convert_crlf_to_lf(str(tmp_path))
    # Verificar que ahora solo tiene LF
    content = file_path.read_bytes()
    assert b'\r\n' not in content
    assert content == b"linea1\nlinea2\nlinea3\n"

    # Crear archivo con solo LF (no debe modificar)
    file_path2 = tmp_path / "test_lf.txt"
    file_path2.write_bytes(b"a\nb\nc\n")
    convert_crlf_to_lf(str(tmp_path))
    content2 = file_path2.read_bytes()
    assert content2 == b"a\nb\nc\n"
