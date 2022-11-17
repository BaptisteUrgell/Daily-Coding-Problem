import argparse

def valid_arr(arr: list, default_arr: list) -> list:
    if not arr:
        return default_arr
    for e in arr:
        if not e in ['R', 'G', 'B']:
            return default_arr
    return arr

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.")

    parser.add_argument('--arr', nargs='*', type=str, metavar='list', default=default_args['arr'], help=f'Original array of R, G, B letter. By default his param is equal to "{default_args["arr"]}"')

    args = parser.parse_args()

    args.arr = valid_arr(args.arr, default_args['arr'])

    return args

def daily(array):
    start, current, end = 0, 0, len(array) - 1

    while current <= end:
        if array[current] == 'R':
            array[start], array[current] = array[current], array[start]
            start += 1
            current += 1
        elif array[current] == 'B':
            array[current], array[end] = array[end], array[current]
            end -= 1
        else:
            current += 1

    print(array)

if __name__ == "__main__":

    default_args = {
        "arr" : ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    }
    args = get_args(default_args)
    daily(args.arr)
