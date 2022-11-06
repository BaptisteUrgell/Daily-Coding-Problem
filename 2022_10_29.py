import argparse

def valid_arr(arr: list, default_arr: list) -> list:
    if not arr:
        return default_arr
    return arr

def valid_k(k: int, default_k: int) -> int:
    if k is None or k < 1:
        return default_k
    return k

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.")

    parser.add_argument('--k', nargs='?', type=int, metavar='int', default=default_args['k'], help=f'Length of subarray. By default his param is equal to "{default_args["k"]}"')
    parser.add_argument('--arr', nargs='*', type=int, metavar='list', default=default_args['arr'], help=f'Original array of integer. By default his param is equal to "{default_args["arr"]}"')

    args = parser.parse_args()

    args.k = valid_k(args.k, default_args['k'])
    args.arr = valid_arr(args.arr, default_args['arr'])

    return args


def daily(arr: list, k: int):
    max_list = [(e, i) for i, e in enumerate(arr[:k])]
    max_list = sorted(max_list, key=lambda x: x[0], reverse=True)
    for i in enumerate(arr[k:]):
        if 
            max_list[]     

if __name__ == "__main__":

    default_args = {
        "k" :  3,
        "arr" : [10, 5, 2, 1, 8, 7]
    }
    args = get_args(default_args)
    daily(args.arr, args.k)

