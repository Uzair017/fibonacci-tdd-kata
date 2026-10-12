"""Tests for the Fibonacci command-line interface."""

import pytest

from fibonacci_tdd_kata.cli import main


def test_cli_prints_fibonacci_number(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["fibonacci", "10"])

    main()

    assert capsys.readouterr().out == "55\n"


def test_cli_prints_zero(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["fibonacci", "0"])

    main()

    assert capsys.readouterr().out == "0\n"


def test_cli_rejects_negative_index(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["fibonacci", "-1"])

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 2
    assert "non-negative" in capsys.readouterr().err.lower()
