import argparse
import time

def valid_n(n: int, default_n: int) -> int:
    if n is None or n < 0:
        return default_n
    return n

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.")

    parser.add_argument('--n', nargs='?', type=int, metavar='int', default=default_args['n'], help=f'Number of millisecond. By default his param is equal to "{default_args["n"]}"')

    args = parser.parse_args()


    args.k = valid_n(args.n, default_args['n'])

    return args

def job():
    print("job is done !")

def daily(f, n: int):
    time.sleep(0.001 * n)
    f()
    
if __name__ == "__main__":

    default_args = {
        "n" : 1000
    }
    args = get_args(default_args)
    daily(job, args.n)

