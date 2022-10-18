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

def daily(tree: Node) -> Node:
    assert deserialize(tree.serialize()).left.left.val == 'left.left'

if __name__ == "__main__":

    default_args = {
        "tree" : Node('root', Node('left', Node('left.left')), Node('right'))
    }

    daily(default_args['tree'])
