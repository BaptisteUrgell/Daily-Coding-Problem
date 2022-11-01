import argparse

def valid_s(s: str, default_s: str) -> str:
    if s is None or len(s) == 0:
        return default_s
    return s

def valid_k(k: int, default_k: int) -> int:
    if k is None or k < 0:
        return default_k
    return k

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.")

    parser.add_argument('--s', nargs='?', type=str, metavar='str', default=default_args['s'], help=f'Original string s. By default his param is equal to "{default_args["s"]}"')
    parser.add_argument('--k', nargs='?', type=int, metavar='int', default=default_args['k'], help=f'Number k of distinct characters. By default his param is equal to "{default_args["k"]}"')

    args = parser.parse_args()


    args.n = valid_s(args.s, default_args['s'])
    args.k = valid_k(args.k, default_args['k'])

    return args

def daily(s: str, k: int):
    u = 0
    n = len(s)

    keys = [chr(num) for num in range(ord('a'), ord('a') + 26)]
    zip_iterator = zip(keys, [0] * len(keys))
    count = dict(zip_iterator)
    curr_start = 0
    curr_end = 0
    max_window_size = 1
    max_window_start = 0

    count[s[0]] += 1
    val = 1

    for i in range(1,n):
        if count[s[i]] == 0:
            val += 1

        count[s[i]] += 1
        curr_end += 1

        while val > k:
            count[s[curr_start]] -= 1
            if count[s[curr_start]] == 0:
                val -= 1
            curr_start += 1
            
        curr_size = curr_end - curr_start + 1
        if curr_size > max_window_size:
            max_window_size = curr_size
            max_window_start = curr_start

    print(s[max_window_start:max_window_start + max_window_size])
    
if __name__ == "__main__":

    default_args = {
        "s" : 'abcba',
        "k" : 2
    }
    args = get_args(default_args)
    daily(args.s, args.k)

