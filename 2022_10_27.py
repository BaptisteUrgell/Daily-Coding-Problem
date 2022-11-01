import argparse
import os

FILE = 'logs.txt'

def valid_id(id: list, default_id: list) -> list:
    if id is None or len(id) == 0:
        return default_id
    return id

def valid_n(n: int, default_n: int) -> int:
    if n is None or n < 0:
        return default_n
    return n

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.")

    parser.add_argument('--n', nargs='?', type=int, metavar='int', default=default_args['n'], help=f'Number k of distinct characters. By default his param is equal to "{default_args["n"]}"')
    parser.add_argument('--id', nargs='*', type=str, metavar='list', default=default_args['id'], help=f'List of id to register in the log structure. By default his param is equal to "{default_args["id"]}"')

    args = parser.parse_args()


    args.n = valid_n(args.n, default_args['n'])
    args.id = valid_id(args.id, default_args['id'])

    return args

def get_last(n):
    list_orderid = []

    with open(FILE, "r") as f:
        for line in f:
            if len(list_orderid) == n:
                list_orderid.pop(0)
            list_orderid.append(line[:-1])

    return list_orderid

def record(order_id: int):
    with open(FILE, "a") as f:
        f.write(order_id + "\n")
    

def daily(n: int, list_id: list):
    for id in list_id: record(id)
    
    last_id = get_last(n)
    print(last_id)

    if os.path.exists(FILE):
        os.remove(FILE)
    
if __name__ == "__main__":

    default_args = {
        "n" : 5,
        "id":  [str(id).zfill(5) for id in range(2)]
    }
    args = get_args(default_args)
    daily(args.n, args.id)

