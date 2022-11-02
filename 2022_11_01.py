import argparse

def valid_t(t: list, default_t: list) -> list:
    if not t:
        return eval(default_t)
    return t

def tuple_int(x: str) -> list:
    return eval(x)

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.")

    parser.add_argument('--t', nargs='?', type=tuple_int, metavar='str', default=default_args['t'], help=f'List of time interval. By default his param is equal to "{default_args["t"]}"')

    args = parser.parse_args()

    args.t = valid_t(args.t, default_args['t'])

    return args

def daily(t: list):
    time = []
    print(t)
    for lecture in t:
       time.append((lecture[0], 1))
       time.append((lecture[1], -1))
    
    if time:
        time.sort(key=lambda x: x[0])

    current, res = 0, 0
    for e in time:
        current += e[1]
        res = max(current, res)
    
    print(res)

if __name__ == "__main__":

    default_args = {
        "t" : "[(30, 75), (0, 50), (60, 150)]"
    }

    args = get_args(default_args)
    daily(args.t)

