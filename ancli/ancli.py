import argparse
import inspect


__all__ = ['Parser', 'add', 'run', 'make_cli']


Parser = argparse.ArgumentParser


def add(parser: Parser, param: dict):
    """Adds new parameter to the parser."""
    param = param.copy()
    name = param.pop('name').replace('_', '-')
    parser.add_argument(f'--{name}', **param)


def run(parser: Parser):
    """Parses the arguments."""
    return vars(parser.parse_args())


def make_cli(func: callable, parser_config: dict = None, spec_only: bool = False):
    parser = Parser(**(parser_config or {}))
    sig = inspect.signature(func)
    spec = []
    for param in sig.parameters.values():
        annot = param.annotation
        options = {}
        if isinstance(annot, tuple):
            ptype, help_msg = annot
            if help_msg is not inspect._empty:
                options['help'] = help_msg
        else:
            ptype = annot
        options['type'] = ptype
        if param.default is inspect._empty:
            options['required'] = True
        else:
            options['default'] = param.default
        options['name'] = param.name
        add(parser, options)
        spec.append(options)
    if spec_only:
        return spec
    else:
        args = run(parser)
        status = func(**args)
        return status
