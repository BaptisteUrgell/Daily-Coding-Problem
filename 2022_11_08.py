# Write an algorithm to justify text. Given a sequence of words and an
# integer line length k, return a list of strings which represents each line,
# fully justified.

def ceil(n: int) -> int:
    if n > int(n):
        n += 1
    return int(n)

def distribute_equally(current: list[str], r: int) -> str:
    line = current[0]
    nb_space = len(current) - 1
    r += nb_space
    for i in range(1, nb_space + 1):
        space = ceil(r/nb_space)
        line += ' ' * space  + current[i]
        r -= space
        nb_space -= 1
    return line

def daily(s: list[str], k: int):
    justified = []
    current = []
    len_line = -1

    for world in s:
        r = k - len_line

        if r <= len(world):
            line = distribute_equally(current, r)
            justified.append(line)
            current = [world]
            len_line = len(world)
        else:
            current.append(world)
            len_line += len(world) + 1

    if current:
        if len(current) > 1:
            r = k - len_line
            line = distribute_equally(current, r)
        else:
            line = current[0] + ' ' * (k - len(current[0]))
        justified.append(line)

    print(justified)        

if __name__ == "__main__":

    default_args = {
        "s" : ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog",],
        'k' : 16
    }

    daily(default_args["s"], default_args["k"])

