import importlib
import sys

from ancli import make_cli


try:
    entry_point = sys.argv[1]
except IndexError:
    print('Error: no entry point name provided!')
    sys.exit(1)

try:
    module_path, function_name = entry_point.split(':')
except ValueError:
    print('Error: entry point name should have format a.b.c:function')
    sys.exit(1)

mod = importlib.import_module(module_path)
try:
    func = getattr(mod, function_name)
except AttributeError:
    print(f'Error: function \'{function_name}\' is not found')
    sys.exit(1)

sys.argv = [sys.argv[0]] + sys.argv[2:]

make_cli(func)
