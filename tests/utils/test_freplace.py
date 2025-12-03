import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from utils.freplace import freplace, freplacefile, freplaceAll

def test_freplace_basic():
    text = "Hola mundo. Mundo!"
    result = freplace(text, "Mundo", "Python")
    assert result == "Hola mundo. Python!"


def test_freplace_no_match():
    text = "Sin coincidencias"
    result = freplace(text, "Nada", "Algo")
    assert result == text


def test_freplacefile(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("foo bar foo")
    freplacefile(str(file_path), "foo", "baz")
    content = file_path.read_text()
    assert content == "baz bar baz"
    file_path.unlink()  # Eliminar fichero temporal


def test_freplacefile_no_match(tmp_path):
    file_path = tmp_path / "test2.txt"
    file_path.write_text("abc def")
    freplacefile(str(file_path), "xyz", "123")
    content = file_path.read_text()
    assert content == "abc def"
    file_path.unlink()  # Eliminar fichero temporal


def test_freplaceAll_text(monkeypatch):
    texto = "SELECT * FROM tabla WHERE id = :ID_EJECUCION"
    monkeypatch.setenv("ID_EJECUCION", "12345")
    resultado = freplaceAll(texto)
    assert resultado == "SELECT * FROM tabla WHERE id = 12345"

def test_freplaceAll_file(tmp_path, monkeypatch):
    file_path = tmp_path / "test2.txt"
    file_path.write_text("UPDATE tabla SET valor = :VALOR", encoding="utf-8")
    monkeypatch.setenv("VALOR", "999")
    freplaceAll(str(file_path))
    contenido = file_path.read_text(encoding="utf-8")
    assert contenido == "UPDATE tabla SET valor = 999"