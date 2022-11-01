import argparse
import random

def valid_e(e: int, default_e: int) -> int:
    if e is None or e < 0:
        return default_e
    return e

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.")

    parser.add_argument('--e', nargs='?', type=int, metavar='int', default=default_args['e'], help=f'Precsision of Pi. By default his param is equal to "{default_args["e"]}"')

    args = parser.parse_args()


    args.e = valid_e(args.e, default_args['e'])

    return args

def daily(e: int):
    circle = 0
    square = int(10**(e*2))

    for _ in range(square):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            circle += 1

        pi = 4 * circle / square
        
    print(pi)
    
if __name__ == "__main__":

    default_args = {
        "e" : 4
    }
    args = get_args(default_args)
    daily(args.e)

