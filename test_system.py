import subprocess
import sys

from main import main


def test_main_con_monkeypatch(monkeypatch, capsys):
    datos = iter(["200", "25"])

    monkeypatch.setattr(
        "builtins.input",
        lambda mensaje: next(datos)
    )

    main()

    salida = capsys.readouterr().out

    assert "Precio con descuento: $150.00" in salida
    assert "Total con IVA: $174.00" in salida


def test_main_subprocess_correcto():
    resultado = subprocess.run(
        [sys.executable, "main.py"],
        input="200\n25\n",
        text=True,
        capture_output=True,
        check=False
    )

    assert resultado.returncode == 0
    assert "Precio con descuento: $150.00" in resultado.stdout
    assert "Total con IVA: $174.00" in resultado.stdout


def test_main_subprocess_descuento_invalido():
    resultado = subprocess.run(
        [sys.executable, "main.py"],
        input="200\n150\n",
        text=True,
        capture_output=True,
        check=False
    )

    assert resultado.returncode == 0
    assert "Error:" in resultado.stdout
    assert "El descuento debe estar entre 0 y 100" in resultado.stdout


def test_main_subprocess_letras():
    resultado = subprocess.run(
        [sys.executable, "main.py"],
        input="abc\n25\n",
        text=True,
        capture_output=True,
        check=False
    )

    assert resultado.returncode == 0
    assert "Error:" in resultado.stdout