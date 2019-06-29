from ancli import make_cli

def run(a, b=2, c=3.0):
    for item in (a, b, c):
        print(type(item))

if __name__ == '__main__':
    make_cli(run)

