import argparse

def valid_s(s: str, default_s: str) -> str:
    if s is None:
        return default_s
    for c in s:
        if not c in "({[]})":
            return default_s
    return s

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).")

    parser.add_argument('--s', nargs='?', type=str, metavar='str', default=default_args['s'], help=f'String of round, curly and square open and closing brackets. By default his param is equal to "{default_args["s"]}"')

    args = parser.parse_args()

    args.s = valid_s(args.s, default_args['s'])

    return args

def daily(s: str) -> bool:
    pile = [""]
    for c in s:
        if c in "({[":
            pile.append(c)
            continue
        if c in ")}]":
            if (c == ")" and pile[-1] == "(") or (c == "}" and pile[-1] == "{") or (c == "]" and pile[-1] == "["):
                pile.pop()
            else:
                return False

    return len(pile) == 1

if __name__ == "__main__":

    default_args = {
        "s" : "([])[]({})",
    }

    args = get_args(default_args)
    print(daily(args.s))

