import argparse

def valid_x(x: list, default_x: list) -> list:
    if not x:
        return default_x
    for e in x:
        if e < 0:
            return default_x
    return x

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.")

    parser.add_argument('--x', nargs='*', type=int, metavar='list', default=default_args['x'], help=f'The two-dimensional elevation map. By default his param is equal to "{default_args["x"]}"')

    args = parser.parse_args()

    args.x = valid_x(args.x, default_args['x'])

    return args

class Wall:
    def __init__(self, left: int, right: int) -> None:
        self.left = left
        self.right = right
        self.length = 0
        self.block = 0
        self.unit = 0

    def min_height(self):
        return min([self.left, self.right])

def daily(x: list):
    wall = Wall(x[0], x[-1])
    for height in x[1:]:
        if wall.left < height:
            wall.unit += wall.left * wall.length - wall.block
            wall.left = height
            wall.block = 0
            wall.length = 0
        elif wall.right <= height:
            wall.unit += height * wall.length - wall.block
            wall.block += height * wall.length - wall.block + height
            wall.length += 1
        else:
            wall.block += height
            wall.length += 1

    print(wall.unit)


if __name__ == "__main__":

    default_args = {
        "x" : [3, 0, 1, 3, 6, 2]
    }
    args = get_args(default_args)
    daily(args.x)

