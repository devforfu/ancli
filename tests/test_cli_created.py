from ancli import make_cli


def test_function_signature_is_correctly_parsed():
    def func(integer: int, floating: float, string: str): pass

    spec = make_cli(func, spec_only=True)

    assert len(spec) == 3
    assert spec[0] == {'name': 'integer', 'type': int, 'required': True}
