import argparse

def valid_s(s: str, default_s: str) -> str:
    if s is None:
        return default_s
    return s

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="he edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.")

    parser.add_argument('--s1', nargs='?', type=str, metavar='str', default=default_args['s1'], help=f'First string. By default his param is equal to "{default_args["s1"]}"')
    parser.add_argument('--s2', nargs='?', type=str, metavar='str', default=default_args['s2'], help=f'Second string. By default his param is equal to "{default_args["s2"]}"')

    args = parser.parse_args()

    args.s1 = valid_s(args.s1, default_args['s1'])
    args.s2 = valid_s(args.s2, default_args['s2'])

    return args

class RunLength:
    def __init__(self):
        pass

    def encode(self, s: str) -> str:
        s_encoded = ""
        count = 1
        char = s[0]
        for c in s[1:]:
            if c == char:
                count += 1
            else:
                s_encoded += str(count) + char
                char = c
                count = 1
        s_encoded += str(count) + char
        return s_encoded

    def decode(self, s: str) -> str:
        s_decode = ""
        for i in range(0, len(s), 2):
            s_decode += int(s[i]) * s[i+1]
        return s_decode

def daily(s1: str, s2: str):
    l = abs(len(s1) - len(s2))
    strings = sorted([s1, s2], key=lambda x: len(x))
    strings[0] += l * ' '
    distance = 0
    for c1, c2 in zip(*strings):
        if not c1 == c2:
            distance += 1
    print(distance)


if __name__ == "__main__":

    default_args = {
        "s1" : "kitten",
        "s2" : "sitting"
    }

    args = get_args(default_args)
    daily(args.s1, args.s2)

