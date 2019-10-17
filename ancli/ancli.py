import argparse
import inspect
import sys


__all__ = ['Parser', 'add', 'run', 'make_cli']


Parser = argparse.ArgumentParser
empty = inspect._empty
_argv = None


def add(parser: Parser, param: dict):
    """Adds new parameter to the parser."""
    param = param.copy()
    name = param.pop('name').replace('_', '-')
    parser.add_argument(f'--{name}', **param)


def set_argv(argv):
    global _argv
    _argv = argv


def run(parser: Parser):
    """Parses the arguments."""
    return vars(parser.parse_args(_argv or sys.argv[1:]))


def make_cli(func: callable,
             parser_config: dict = None,
             spec_only: bool = False,
             show_params: bool = False):
    """Wraps Python function with CLI.

    Args:
        func: Function to wrap.
        parser_config: Parameters directly delegated to argparse.ArgumentParser.
        spec_only: Don't create CLI and only print meta-information extracted
            from function. Useful for debugging.
        show_params: If True, then the parameters passed into function are
            printed right before its call. Ignored if `spec_only` parameter is
            provided.

    """
    parser = Parser(**(parser_config or {}))
    sig = inspect.signature(func)
    spec = []
    for param in sig.parameters.values():
        annot = param.annotation
        options = {}
        if annot is empty:
            ptype = str
        elif isinstance(annot, tuple):
            ptype, help_msg = annot
            if help_msg is not empty:
                options['help'] = help_msg
        else:
            ptype = annot
        options['type'] = ptype
        if param.default is empty:
            options['required'] = True
        else:
            options['default'] = param.default
            if annot is empty:
                options['type'] = type(options['default'])
        options['name'] = param.name
        add(parser, options)
        spec.append(options)
    if spec_only:
        return spec
    else:
        args = run(parser)
        print('invoked with parameters')
        print('-----------------------')
        if show_params:
            for k, v in args.items():
                print(f'{k}={v}')
        status = func(**args)
        return status
