import sys
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
