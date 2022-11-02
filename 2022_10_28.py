import argparse

def valid_string(string: str, default_string: str) -> str:
    if string is None:
        return default_string
    return string.replace("\\n", "\n").replace("\\t", "\t")

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.")

    parser.add_argument('--string', nargs='?', type=str, metavar='str', default=default_args['string'], help=f'String representation of system files. By default his param is equal to "{default_args["string"]}"')

    args = parser.parse_args()

    args.string = valid_string(args.string, default_args['string'])

    return args

def length_pathfile(string: str) -> int:
    max_length = 0
    current_length = 0
    length_level = [0, 0]
    level = 1
    i = 0

    while i < len(string):
        if string[i] == ".":
            while i < len(string) and not string[i] == "\n":
                current_length += 1
                i += 1
            max_length = max(max_length, length_level[level-1] + current_length)
            i -= 1
        
        if string[i] == '\n':
            if len(length_level) <= level:
                length_level.append(0)
            length_level[level] = length_level[level-1] + current_length
            level = 1

        if string[i] == '\t':
            level += 1
            current_length = 0
        
        i += 1
        current_length += 1
    return max_length

def daily(string: str):
    length = length_pathfile(string)
    print(string)
    print(length)

    
if __name__ == "__main__":

    default_args = {
        "string":  "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    }
    args = get_args(default_args)
    daily(args.string)

