from ancli import make_cli


def test_function_signature_with_all_required_params():
    def all_required(integer: int, floating: float, string: str): pass

    spec = make_cli(all_required, spec_only=True)

    assert len(spec) == 3
    assert spec[0] == {'name': 'integer', 'type': int, 'required': True}
    assert spec[1] == {'name': 'floating', 'type': float, 'required': True}
    assert spec[2] == {'name': 'string', 'type': str, 'required': True}


def test_function_signature_with_default_params():
    def all_optional(x: int = 1, y: int = 2, z: int = 3): pass

    spec = make_cli(all_optional, spec_only=True)

    assert len(spec) == 3
    assert spec[0] == {'name': 'x', 'type': int, 'default': 1}
    assert spec[1] == {'name': 'y', 'type': int, 'default': 2}
    assert spec[2] == {'name': 'z', 'type': int, 'default': 3}


def test_function_signature_with_required_and_default_params():
    def some_optional(first: int, second: bool = False): pass

    spec = make_cli(some_optional, spec_only=True)

    assert len(spec) == 2
    assert spec[0] == {'name': 'first', 'type': int, 'required': True}
    assert spec[1] == {'name': 'second', 'type': bool, 'default': False}


def test_function_signature_without_args():
    def no_args(): pass

    spec = make_cli(no_args, spec_only=True)

    assert not spec
