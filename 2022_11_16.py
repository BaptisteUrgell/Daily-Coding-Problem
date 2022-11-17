import argparse

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

def create_node(list_tree: list[str]) -> tuple[Node, int]:
    if list_tree[0] == 'null':
        return None, 2

    left, nb_sub_node_left = create_node(list_tree[1:])
    right, nb_sub_node_right = create_node(list_tree[nb_sub_node_left:])
    nb_sub_node = nb_sub_node_left + nb_sub_node_right
    return Node(int(list_tree[0]), left, right), nb_sub_node

def deserialize(str_tree: str) -> Node:
    list_tree = str_tree.split(' ')
    tree, _ = create_node(list_tree)
    return tree

def findSecondLargestNode(node: Node, max_array):
	if node is None:
		return max_array

	max_array.append(node.val)
	max_array = sorted(max_array, reverse=True)[:2]

	max_array = findSecondLargestNode(node.right, max_array)
	max_array += findSecondLargestNode(node.left, max_array)
	max_array = list(dict.fromkeys(max_array))
	max_array = sorted(max_array, reverse=True)[:2]
	return max_array

def daily(tree: Node) -> int:
	print_tree(tree)
	max_array = findSecondLargestNode(tree, [tree.val] * 2)
	print()
	print(min(max_array))

def valid_tree(tree: Node, default_tree: Node) -> Node:
    if tree is None:
        return deserialize(default_tree)
    return tree

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given the root to a binary search tree, find the second largest node in the tree.")

    parser.add_argument('--tree', nargs="?", type=deserialize, metavar='tree', default=default_args['tree'], help=f'list of nodes. By default his param is equal to "{default_args["tree"]}"')
    
    args = parser.parse_args()

    args.tree = valid_tree(args.tree, default_args['tree'])
    return args

if __name__ == "__main__":

    default_args = {
        "tree" : "11 2 8 9 null null 10 null null 1 12 null null null 3 4 5 null null 6 null null 7 null null"
    }

    args = get_args(default_args)
    daily(args.tree)

