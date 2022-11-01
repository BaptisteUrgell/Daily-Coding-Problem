import argparse

def valid_list(list_int: list[int], default_list_int: list[int]) -> list[int]:    
    if list_int:
        return list_int
    else:
        return default_list_int

def valid_k(k: int, default_k: int) -> int:
    if k is None:
        return default_k
    else:
        return k

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given a list of numbers and a number k, return whether any two numbers from the list add up to k.")

    parser.add_argument('--list', nargs='*', type=int, metavar='list[int]', default=default_args['list_int'], help=f'list of numbers. By default his param is equal to "{default_args["list_int"]}"')
    parser.add_argument('--k', nargs='?', type=int, metavar='int', default=default_args['k'], help=f'Number k. By default his param is equal to "{default_args["k"]}"')

    args = parser.parse_args()

    args.list = valid_list(args.list, default_args['list_int'])
    args.k = valid_k(args.k, default_args['k'])

    return args

def daily(list_int: list[int], k: int) -> bool:
    res = False
    dict_int = dict()
    for e in list_int:
        if (k - e) in dict_int:
            res = True 
        dict_int[e] = None
    
    print(res)

if __name__ == "__main__":

    default_args = {
        "list_int" : [10, 15, 3, 7],
        "k"      : 17
    }
    args = get_args(default_args)
    daily(args.list, args.k)

