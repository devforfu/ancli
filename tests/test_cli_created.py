from ancli import make_cli


def some_required(a: int, b: bool = True): pass


def none_required(x=1, y=2, z=3): pass


def no_args(): pass


def test_function_signature_with_all_required_params():
    def all_required(integer: int, floating: float, string: str): pass

    spec = make_cli(all_required, spec_only=True)

    assert len(spec) == 3
    assert spec[0] == {'name': 'integer', 'type': int, 'required': True}
    assert spec[1] == {'name': 'floating', 'type': float, 'required': True}
    assert spec[2] == {'name': 'string', 'type': str, 'required': True}
