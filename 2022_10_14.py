import argparse
from ast import arg

def print_tree(root, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self):
        left = self.left.serialize() if not self.left is None else 'null'
        right = self.right.serialize() if not self.right is None else 'null'
        return str(self.val) + ' ' + left + ' ' + right
        

def create_node(list_tree: list[str]) -> tuple[Node, int]:
    if list_tree[0] == 'null':
        return None, 2

    left, nb_sub_node_left = create_node(list_tree[1:])
    right, nb_sub_node_right = create_node(list_tree[nb_sub_node_left:])
    nb_sub_node = nb_sub_node_left + nb_sub_node_right
    return Node(list_tree[0], left, right), nb_sub_node

def deserialize(str_tree: str) -> Node:
    list_tree = str_tree.split(' ')
    tree, _ = create_node(list_tree)
    return tree

def daily(tree: Node):
    print_tree(tree)
    print()
    str_tree = tree.serialize()
    print("serialize   :", str_tree)
    print()
    print("deserialize :")
    tree = deserialize(str_tree)
    print_tree(tree)

def valid_tree(tree: Node, default_tree: Node) -> Node:
    if tree is None:
        return deserialize(default_tree)
    return tree

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.")

    parser.add_argument('--tree', nargs="?", type=deserialize, metavar='tree', default=default_args['tree'], help=f'list of nodes. By default his param is equal to "{default_args["tree"]}"')
    
    args = parser.parse_args()

    args.tree = valid_tree(args.tree, default_args['tree'])
    return args

if __name__ == "__main__":

    default_args = {
        "tree" : "root left left.left null null null right null null"
    }

    args = get_args(default_args)
    daily(args.tree)
