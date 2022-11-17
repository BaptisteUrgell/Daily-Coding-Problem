import argparse
from math import log

def valid_x(x: list, default_x: list) -> list:
    if not x:
        return default_x
    for sub_x in x:
        if not len(x) == len(sub_x):
            return default_x
    return x

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.")

    parser.add_argument('--x', nargs='*', type=int, metavar='list', default=default_args['x'], help=f'Table of currency exchange rates. By default his param is equal to "{default_args["x"]}"')

    args = parser.parse_args()

    args.x = valid_x(args.x, default_args['x'])

    return args

def transform(w: list) -> list:
    n = len(w)
    for i in range(n):
        for j in range(n):
            if isinstance(w[i][j], (float, int)): w[i][j] = -log(w[i][j]) 
    return w

def floydWarshall(w: list) -> list:
    n = len(w)
    w = transform(w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if isinstance(w[i][k], (int, float)) and isinstance(w[k][j], (int, float)):
                    if w[i][j] is None: w[i][j] = w[i][k] + w[k][j]
                    w[i][j] = min(w[i][j], w[i][k] + w[k][j])
    return w

def daily(x: list):
    x = floydWarshall(x)
    print(x)
    

if __name__ == "__main__":

    default_args = {
        "x" : [[1, 1, 1, None], [None, 0.9, 1.1, None], [0.8, 1.2, None, 0.7], [1, 0.6, 1, 0.7]]
    }
    args = get_args(default_args)
    daily(args.x)

