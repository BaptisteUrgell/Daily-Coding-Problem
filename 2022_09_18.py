import argparse
import json

def valid_code(code: str, default_code: str) -> str:
    if not (code is None) and int(code) > 0:
        return code
    else:
        return default_code

def valid_map(mapping: dict, default_map: dict) -> dict:
    if mapping is None:
        return default_map

    for key in mapping:
        if not key.isdigit():
            return default_map
    return mapping

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.")

    parser.add_argument('--code', nargs='?', type=str, metavar='str', default=default_args['code'], help=f'Encoded message. By default his param is equal to "{default_args["code"]}"')
    parser.add_argument('--map', nargs='?', type=json.loads, metavar='dict', default=default_args['map'], help=f'Decoder map. By default his param is equal to "{default_args["map"]}"')
    args = parser.parse_args()

    args.code = valid_code(args.code, default_args['code'])
    args.map = valid_map(args.map, default_args['map'])

    return args

def daily(code: str, mapping: dict()) -> int:
    ways = [1, 1]
    for i in range(1, len(code)):
        w = 0

        if code[i] in mapping:
            w += ways[0]

        if code[i-1:i+1] in mapping:
            w += ways[1]

        ways[1] = ways[0]
        ways[0] = w
        
    return ways[0]
    
if __name__ == "__main__":
    letters = [chr(num) for num in range(97, 97 + 26)]
    keys = [str(num) for num in range(1, 27)]
    zip_iterator = zip(keys, letters)

    default_args = {
        "code" : '111',
        "map" : dict(zip_iterator)
    }

    args = get_args(default_args)
    print(daily(args.code, args.map))
