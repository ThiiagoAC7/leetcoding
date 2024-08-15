# 14/08
# Given the root to a binary tree,
# - implement serialize(root), which serializes the tree into a string,
# - and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root : Node):

    stack = [root]
    l_str = []


    while stack:
        node = stack.pop()

        if node != None:
            l_str.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        else:
            l_str.append("-")


    return ",".join(l_str)

def deserialize(s : str):
    l_str = s.split(',')
    t = _rebuild_tree(l_str, 0)
    return t


def _rebuild_tree(arr, idx):

    if arr[idx] == '-':
        return None 

    node = Node(arr[idx])
    node.left = _rebuild_tree(arr, idx+1)

    return node 


def test_case_01():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
