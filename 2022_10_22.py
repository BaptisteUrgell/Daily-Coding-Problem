import argparse
import re

def valid_dict(dictionary: list, default_dict: list) -> list:
    if not dictionary:
        return default_dict
    return dictionary

def valid_string(string: str, default_string: str) -> str:
    if string is None:
        return default_string
    return string

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.")

    parser.add_argument('--dict', nargs='*', type=str, metavar='int', default=default_args['dict'], help=f'Dictionary. By default his param is equal to "{default_args["dict"]}"')
    parser.add_argument('--string', nargs='?', type=str, metavar='str', default=default_args['string'], help=f'String to fine. By default his param is equal to "{default_args["string"]}"')

    args = parser.parse_args()


    args.dict = valid_dict(args.dict, default_args['dict'])
    args.string = valid_string(args.string, default_args['string'])

    return args


def daily(string: str, dictionary: list):
    pattern = re.compile(string)
    print([word for word in dictionary if pattern.match(word)])
    
    
if __name__ == "__main__":

    default_args = {
        "dict" :  ['dog', 'deer', 'deal'],
        "string" : "de"
    }
    args = get_args(default_args)
    daily(args.string, args.dict)

