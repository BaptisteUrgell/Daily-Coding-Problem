import argparse

def valid_list(list_int: list[int], default_list_int: list[int]) -> list[int]:    
    if list_int:
        return list_int
    return default_list_int

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.")

    parser.add_argument('--list', nargs='*', type=int, metavar='list[int]', default=default_args['list_int'], help=f'list of numbers. By default his param is equal to "{default_args["list_int"]}"')

    args = parser.parse_args()

    args.list = valid_list(args.list, default_args['list_int'])

    return args

def daily(list_int: list[int]):
    dyn_sum = [[0, list_int[0]]]
    
    for i in range(1, len(list_int)):
        sub_sum = dyn_sum[-1]
        _max = max(sub_sum)
        sub_sum[1] = sub_sum[0] + list_int[i]
        sub_sum[0] = _max
        dyn_sum.append(sub_sum)

    print(max(dyn_sum[-1]))

if __name__ == "__main__":

    default_args = {
        "list_int" : [2, 4, 6, 2, 5]
    }
    args = get_args(default_args)
    daily(args.list)