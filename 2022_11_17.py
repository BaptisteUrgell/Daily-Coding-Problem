import argparse

def valid_s(s: list, default_s: list) -> list:
    if not s:
        return default_s
    return s

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.")

    parser.add_argument('--s', nargs='*', type=int, metavar='list', default=default_args['s'], help=f'The given set. By default his param is equal to "{default_args["s"]}"')

    args = parser.parse_args()

    args.s = valid_s(args.s, default_args['s'])

    return args

def PowerSet(s):
    add_set, remove_set = [[]], [s]

    for i in range(len(s)//2 + 1):
        for j in range(len(add_set)):
            add_set.append(add_set[j] + [s[i]])
            sub_set = [x for x in remove_set[j] if not x == s[i]]
            remove_set.append(sub_set)
    return add_set + remove_set

def daily(s: list):
    power_set = PowerSet(s)
    print(power_set)

if __name__ == "__main__":

    default_args = {
        "s" : [1, 2, 3,]
    }
    args = get_args(default_args)
    daily(args.s)
