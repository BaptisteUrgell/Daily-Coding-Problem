import argparse
from heapq import heappush, heappop, heapify
import math

def valid_stream(stream: list[int], default_stream: list[int]) -> list[int]:
    if stream is None:
        return default_stream
    return stream

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.")

    parser.add_argument('--stream', nargs='*', type=int, metavar='list', default=default_args['stream'], help=f'The stream. By default his param is equal to "{default_args["stream"]}"')

    args = parser.parse_args()


    args.stream = valid_stream(args.stream, default_args['stream'])

    return args


def daily(stream):

    upper = []
    lower = []
    for e in stream:
        heappush(lower, -e)
        heappush(upper, -heappop(lower))

        if len(upper) > len(lower):
            heappush(lower, -heappop(upper))

        if len(upper) != len(lower):
            print(-lower[0])
        else:
            print((upper[0] - lower[0])/2)

if __name__ == "__main__":

    default_args = {
        "stream" : [2, 1, 5, 7, 2, 0, 5]
    }

    args = get_args(default_args)
    daily(args.stream)

