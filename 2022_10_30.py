import argparse

def valid_m(m: list, default_m: list) -> list:
    if m is None or len(m) == 0:
        return eval(default_m)
    return eval(m)

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.")

    parser.add_argument('--m', nargs='?', type=str, metavar='str', default=default_args['m'], help=f'Matrix of color and cost. By default his param is equal to "{default_args["m"]}"')

    args = parser.parse_args()


    args.m = valid_m(args.m, default_args['m'])

    return args

def min_cost(color_cost: list, prev_cost: int, exclude: int = -1) -> tuple[float, int]:
    count, cost, color = None, None, None

    for i in range(len(color_cost)):
        if i == exclude: continue
        if cost is None : count, cost, color = 0, color_cost[i], i
        if cost == color_cost[i]: count += 1
        if cost >= color_cost[i]: count, cost, color = 0, color_cost[i], i
    
    if count > 0: color = None

    return prev_cost + cost, color

def daily(m: list):
    way1, way2 = (0, None), (0, None)
    
    for color_cost in m:
        if way1[1] is None:
            way2, way1 = way1, min_cost(color_cost, way1[0])
            if not way1[1] is None: way2 = min_cost(color_cost, way2[0], way1[1])
        else:
            way1 = min_cost(color_cost, way1[0], way1[1])
            if way2[1] is None: 
                way2 = min_cost(color_cost, way2[0])
            else: 
                way2 = min_cost(color_cost, way2[0], way2[1])
        
        if way1[0] == way2[0]: way1, way2 = (way1[0], None), (way2[0], None)
        if way1[0] > way2[0]: way1, way2 = way2, way1

    print(min(way1[0], way2[0]))
    
if __name__ == "__main__":

    default_args = {
        "m" : '[[1,2,3,4,5], [3,1,3,4,5], [1,2,3,4,5], [4,10,2,2,5]]'
    }
    args = get_args(default_args)
    daily(args.m)

