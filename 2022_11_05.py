import argparse

def valid_re(re: str, default_re: str) -> str:
    if not re or len(re) == 0:
        return default_re
    return re

def valid_s(s: str, default_s: str) -> str:
    if s is None or len(s) == 0:
        return default_s
    return s

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Implement regular expression matching with the following special characters: (period) which matches any single character (asterisk) which matches zero or more of the preceding element")

    parser.add_argument('--s', nargs='?', type=str, metavar='str', default=default_args['s'], help=f'Word to test. By default his param is equal to "{default_args["s"]}"')
    parser.add_argument('--re', nargs='?', type=str, metavar='str', default=default_args['re'], help=f'Regular expression to use. By default his param is equal to "{default_args["re"]}"')

    args = parser.parse_args()

    args.re = valid_re(args.re, default_args['re'])
    args.s = valid_s(args.s, default_args['s'])

    return args

def daily(pattern: str, text: str) -> bool:
    n, m = len(text), len(pattern)
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        if pattern[i - 1] == "*":
            dp[0][i] = dp[0][i - 2]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[j - 1] == "." or pattern[j - 1] == text[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == "*":
                dp[i][j] = dp[i][j - 2]
                if pattern[j - 2] == "." or pattern[j - 2] == text[i - 1]:
                    dp[i][j] = dp[i][j] | dp[i - 1][j]
    return dp[n][m]

if __name__ == "__main__":

    default_args = {
        "s" : "chat",
        "re" : ".*.at."
    }

    args = get_args(default_args)
    print(daily(args.re, args.s))

