import argparse

def valid_x(x: list, default_x: list) -> list:
    if not x:
        return default_x
    for e in x:
        if e <= 0:
            return default_x
    return x

def valid_n(n: int, default_n: int) -> int:
    if n is None or n < 0:
        return default_n
    return n

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.")

    parser.add_argument('--n', nargs='?', type=int, metavar='int', default=default_args['n'], help=f'Staircase with N steps. By default his param is equal to "{default_args["n"]}"')
    parser.add_argument('--x', nargs='*', type=int, metavar='list', default=default_args['x'], help=f'Number of step that you can climb. By default his param is equal to "{default_args["x"]}"')

    args = parser.parse_args()


    args.n = valid_n(args.n, default_args['n'])
    args.x = valid_x(args.x, default_args['x'])

    return args

def find_ways(x: list, n: int):
    nb_ways = 0
    for e in x:
        sub_n = n - e
        if sub_n > 0:
            nb_ways += find_ways(x, sub_n)
        if sub_n == 0:
            nb_ways += 1
    return nb_ways


def daily(x: list, n: int):
    nb_ways = find_ways(x, n)
    print(nb_ways)    
    
if __name__ == "__main__":

    default_args = {
        "n" :  4,
        "x" : [1, 2]
    }
    args = get_args(default_args)
    daily(args.x, args.n)

