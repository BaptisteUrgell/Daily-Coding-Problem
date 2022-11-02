import argparse

def valid_d(d: list, default_d: list) -> list:
    if not d:
        return set(default_d)
    return set(d)

def valid_s(s: str, default_s: str) -> str:
    if s is None or len(s) == 0:
        return default_s
    return s

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.")

    parser.add_argument('--d', nargs='*', type=str, metavar='list', default=default_args['d'], help=f'Dictionary of words. By default his param is equal to "{default_args["d"]}"')
    parser.add_argument('--s', nargs='?', type=str, metavar='str', default=default_args['s'], help=f'Sentence made up with the dict world. By default his param is equal to "{default_args["s"]}"')

    args = parser.parse_args()

    args.d = valid_d(args.d, default_args['d'])
    args.s = valid_s(args.s, default_args['s'])

    return args

def daily(d: set, s: str):
    list_word = [[""]]
    max_length = len(max(d, key=lambda x: len(x)))

    for c in s:
        for i in range(len(list_word)):
            list_word[i][-1] += c
            if list_word[i][-1] in d:
                list_word.append(list_word[i].copy())
                list_word[i].append("")
        i = 0
        while i < len(list_word):
            if len(list_word[i][-1]) >= max_length:
                list_word.pop(i)
            i += 1

    print(next((words[:-1] for words in list_word), None))

if __name__ == "__main__":

    default_args = {
        "d" : ['bed', 'bath', 'bedbath', 'and', 'beyond', 'hello', 'kaggle', 'python', 'golden', 'dog', 'cat', 'goldenbed'],
        "s" : "goldenbedbathdogandbeyondpythonhellokagglecat"
    }
    
    args = get_args(default_args)
    daily(args.d, args.s)

