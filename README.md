# ancli
Building argument parser from a function annotation. A simple utility inspired by 
`Fire` and `docopt`. Ad-hoc solution for someone who often writes scripts with a 
single entry point.

## How?

The process of building CLI with `ancli` is very simple.
1. Write a plain Python function with annotated parameters.
2. Wrap it with `make_cli`.
3. Run your script.


## Examples

### 1. Function with annotated parameters

The function `run` has explicitly annotated parameters and its signature is used 
to instantiate `argparse.ArgumentParser` instance that accepts parameters with 
specific types and default (if any) parameters. If default value is not provided,
then the parameter is considered to be required.
```python
from ancli import make_cli

def run(path: str, flag: bool = True, iterations: int = 1):
    print(f'run: path={path}, flag={flag}, iterations={iterations}')
    
if __name__ == '__main__':
    make_cli(run)
```
Now this snippet can be used as follows.
```bash
$ python script.py --path file.txt --flag 0
run: path=file.txt, flag=False, iterations=1
```

### 2. Function without annotations

The functions without type annotations try to infer the parameters types based
on their default values.
```python
from ancli import make_cli

def run(a, b=2, c=3.0):
    for param in (a, b, c):
        print(type(param))

if __name__ == '__main__':
    make_cli(run)
```
The parameters without default values are considered as strings.
```bash
$ python script.py --a 1 --b 2 --c 3.0
<type 'str'>
<type 'int'>
<type 'float'>
```
