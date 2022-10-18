import argparse

def valid_num(num: int, default_num: int) -> int:
    if num is None:
        return default_num
    else:
        return num

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.")

    parser.add_argument('--a', nargs='?', type=int, metavar='int', default=default_args['a'], help=f'First number of the pair. By default his param is equal to "{default_args["a"]}"')
    parser.add_argument('--b', nargs='?', type=int, metavar='int', default=default_args['b'], help=f'Second number of the pair. By default his param is equal to "{default_args["b"]}"')

    args = parser.parse_args()
    args.a = valid_num(args.a, default_args['a'])
    args.b = valid_num(args.b, default_args['b'])
    return args

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair) -> int:
    return pair(lambda x, _: x)

def cdr(pair) -> int:
    return pair(lambda _, x: x)

def daily(a: int, b: int) -> None:
    print(f'car(cons({a},{b}))', car(cons(a,b)))
    print(f'cdr(cons({a},{b}))', cdr(cons(a,b)))

    return None

if __name__ == "__main__":
    default_args = {
        "a" : 3,
        "b" : 4
    }
    args = get_args(default_args)
    daily(args.a, args.b)