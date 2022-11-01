import argparse

def valid_list(list_int: list[int], default_list_int: list[int]) -> list[int]:    
    if list_int:
        return list_int
    else:
        return default_list_int

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.")

    parser.add_argument('--list', nargs='*', type=int, metavar='list[int]', default=default_args['list_int'], help=f'list of numbers. By default his param is equal to "{default_args["list_int"]}"')

    args = parser.parse_args()

    args.list = valid_list(args.list, default_args['list_int'])

    return args

def daily(list_int: list[int]) -> list[int]:
    
    forward = [list_int[0]]
    backward = [list_int[-1]]
    for i in range(1, len(list_int)):
        forward.append(forward[i-1] * list_int[i])
        backward.append(backward[i-1] * list_int[-i-1])

    prod = [backward[-2]]
    for i in range(1, len(list_int) - 1):
        prod.append(forward[i-1] * backward[-i-2])
    prod.append(forward[-2])

    print(prod)
    
if __name__ == "__main__":

    default_args = {
        "list_int" : [1, 2, 3, 4, 5]
    }
    args = get_args(default_args)
    daily(args.list)

