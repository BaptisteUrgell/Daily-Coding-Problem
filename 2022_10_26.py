import argparse
import random


def valid_stream(stream: str, default_stream: str) -> str:
    if stream is None:
        return default_stream
    return stream

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.")

    parser.add_argument('--stream', nargs='?', type=str, metavar='str', default=default_args['stream'], help=f'The stream. By default his param is equal to "{default_args["stream"]}"')

    args = parser.parse_args()


    args.e = valid_stream(args.stream, default_args['stream'])

    return args

def daily(stream):
    random_e = None
    for i, e in enumerate(stream):
        if i == 0:
            random_e = e
        elif random.randint(0, i) == 0:
            random_e = e
    
    print(random_e)


if __name__ == "__main__":

    default_args = {
        "stream" : "It_is_a_stream."
    }

    args = get_args(default_args)
    daily(args.stream)

