import contextlib
import io
import sys
import textwrap
from ancli import make_cli


def test_building_cli_from_function(monkeypatch):
    monkeypatch.setattr(sys, 'argv', [
        'entry_point',
        '--command', 'run',
        '--path', 'file.txt',
        '--flag', '1',
    ])

    params = {}

    def run(command: str, path: str = 'default.txt', flag: bool = False):
        nonlocal params
        params['command'] = command
        params['path'] = path
        params['flag'] = flag

    make_cli(run)

    assert len(params) == 3
    assert params['command'] == 'run'
    assert params['path'] == 'file.txt'
    assert params['flag']


def test_printing_parameters_passed_info_function(monkeypatch):
    monkeypatch.setattr(sys, 'argv', [
        'entry_point',
        '--first', 'a',
        '--second', 'b',
        '--third', 'c'
    ])

    expected_output = textwrap.dedent('''
    invoked with parameters
    -----------------------
    first=a
    second=b
    third=c
    ''')

    def run(first: str, second: str, third: str):
        pass

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        make_cli(run, show_params=True)

    captured = buf.getvalue()
    assert captured == expected_output[1:]  # exclude first newline char
