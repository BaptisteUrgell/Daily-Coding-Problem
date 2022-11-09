import argparse

def valid_s(s: str, default_s: str) -> str:
    if s is None:
        return default_s
    for c in s:
        if ord(c) > 47 and ord(c) < 58:
            return default_s
    return s

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character.")

    parser.add_argument('--s', nargs='?', type=str, metavar='str', default=default_args['s'], help=f'String to be Run-lenght encoded, curly and square open and closing brackets. By default his param is equal to "{default_args["s"]}"')

    args = parser.parse_args()

    args.s = valid_s(args.s, default_args['s'])

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

def daily(s: str):
    runlength = RunLength()
    s_encoded = runlength.encode(s)
    print(s_encoded)
    s_decoded = runlength.decode(s_encoded)
    print(s_decoded)

if __name__ == "__main__":

    default_args = {
        "s" : "AAAA111BBBCCDAA",
    }

    args = get_args(default_args)
    daily(args.s)

