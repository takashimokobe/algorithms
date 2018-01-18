class BinarySearchTree:
    def __init__(self, comes_before, tree=None):
        self.comes_before = comes_before  # a function
        self.tree = tree                  # a BST Tree

    def __repr__(self):
        return "BinarySearchTree({!r})".format(self.tree)

    def __eq__(self, other):
        return (type(other) == BinarySearchTree
                and self.comes_before == other.comes_before
                and self.tree == other.tree)


class BSTNode:
    def __init__(self, value, left, right):
        self.value = value  # a int/float
        self.left = left    # a BSTnode
        self.right = right  # a BSTnode

    def _repr__(self):
        return "BSTNode({!r}, {!r}, {!r})".format(self.value, self.left, self.right)

    def __eq__(self, other):
        return (type(other) == BSTNode
                and self.value == other.value
                and self.left == other.left
                and self.right == other.right)


# BinarySearchTree -> bool
# determines if the tree is empty
def is_empty(bst):
    if (bst.tree is None):
        return True
    else:
        return False


def insert_helper(bstNode, val, f):
    if bstNode is None:
        return BSTNode(val, None, None)
    else:
        if f(val, bstNode.value) is True:
            return BSTNode(bstNode.value, insert_helper(bstNode.left, val, f), bstNode.right)
        else:
            return BSTNode(bstNode.value, bstNode.left, insert_helper(bstNode.right, val, f))


# BinarySearchTree val -> BinarySearchTree
# returns a tree with the value appropriately inserted
def insert(bst, val):
    return BinarySearchTree(bst.comes_before, insert_helper(bst.tree, val, bst.comes_before))

# lookup helper
# Node value f -> bool
# determines if a value is in a tree
def lookup_helper(bstNode, val, f):
    if bstNode is None:
        return False
    else:
        if not f(val, bstNode.value) and not f(bstNode.value, val):
            return True
        elif f(val, bstNode.value) is True:
            return lookup_helper(bstNode.left, val, f)
        else:
            return lookup_helper(bstNode.right, val, f)


def lookup(bst, val):
    return lookup_helper(bst.tree, val, bst.comes_before)


# delete helper
def get_right_min(tree):
    if tree.left is None:
        return tree.value
    else:
        return get_right_min(tree.left)


# delete helper
def delete_right_min(tree):
    if tree.left is None:
        return None
    return BSTNode(tree.value, delete_right_min(tree.left), tree.right)


# delete helper
# deletes a value from a tree
def delete_helper(tree, val, f):
    if tree is None:
        return None
    elif not f(tree.value, val) and not f(val, tree.value):
        if tree.left is None and tree.right is None:
            return None
        elif tree.right is None:
            return tree.left
        elif tree.left is None:
            return tree.right
        else:
            return BSTNode(get_right_min(tree.right), tree.left, delete_right_min(tree.right))
    elif f(val, tree.value) is True:
        return BSTNode(tree.value, delete_helper(tree.left, val, f), tree.right)
    else:
        return BSTNode(tree.value, tree.left, delete_helper(tree.right, val, f))


# BinarySearchTree val -> BinarySearchTree
# deletes the value from the tree | assumes it is present
def delete(bst, val):
    return BinarySearchTree(bst.comes_before, delete_helper(bst.tree, val, bst.comes_before))


# PREfix iterator
# BinarySearchTree -> Iterator
# returns an iterator of the elements in prefix order
def prefix_iterator(bst):
    if bst.tree is not None:
        yield bst.tree.value
        yield from prefix_iterator(BinarySearchTree(bst.comes_before, bst.tree.left))
        yield from prefix_iterator(BinarySearchTree(bst.comes_before, bst.tree.right))


# POSTfix iterator
# BinarySearchTree -> Iterator
# returns an iterator of the elements in postfix order
def postfix_iterator(bst):
    if bst.tree is not None:
        yield from postfix_iterator(BinarySearchTree(bst.comes_before, bst.tree.right))
        yield from postfix_iterator(BinarySearchTree(bst.comes_before, bst.tree.left))
        yield bst.tree.value


def infix_iterator(bst):
    if bst.tree is not None:
        yield from infix_iterator(BinarySearchTree(bst.comes_before, bst.tree.left))
        yield bst.tree.value
        yield from infix_iterator(BinarySearchTree(bst.comes_before, bst.tree.right))


