import argparse

def valid_list(list_int: list[int], default_list_int: list[int]) -> list[int]:    
    if list_int:
        return list_int
    else:
        return default_list_int

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.")

    parser.add_argument('--list', nargs='*', type=int, metavar='list[int]', default=default_args['list_int'], help=f'list of numbers. By default his param is equal to "{default_args["list_int"]}"')

    args = parser.parse_args()

    args.list = valid_list(args.list, default_args['list_int'])

    return args

def daily(list_int: list[int]):
    i = 0
    n = len(list_int)
    while i < n:
        j = list_int[i]
        if 0 < j < n and j != list_int[j - 1]:
            list_int[i], list_int[j - 1] = list_int[j - 1], list_int[i]
        else:
            i += 1

    print(next((x + 1 for x in range(n) if list_int[x] != x + 1), n + 1))

if __name__ == "__main__":

    default_args = {
        "list_int" : [3, 4, -1, 1]
    }
    args = get_args(default_args)
    daily(args.list)