# A Binary tree of numbers one of
# Empty, or 
# a Node(value, left, right)

class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return ((type(other) == TreeNode)
          and self.value == other.value
          and self.left == other.left
          and self.right == other.right
        )

    def __repr__(self):
        return ("TreeNode({!r}, {!r}, {!r})".format(self.value, self.left, self.right))

# BinaryTree -> int
# takes in a BinaryTree and returns the number of values/elements
def size(treeNode):
  if (treeNode == "mt"):
    return 0
  else:
    return 1 + size(treeNode.left) + size(treeNode.right)

# BinaryTree -> int 
# takes in a BinaryTree that returns the number of leaves (nodes with both subtrees empty) 
def num_leaves(treeNode):
  if (treeNode == "mt"):
    return 0
  elif treeNode.left == "mt" and treeNode.right == "mt":
    return 1
  else:
    return num_leaves(treeNode.left) + num_leaves(treeNode.right)


#BinaryTree -> int 
# takes in a BinaryTree and returns the sum of the values in the tree
def sum(treeNode):
  if (treeNode == "mt"):
    return 0
  else:
    return treeNode.value + sum(treeNode.left) + sum(treeNode.right)

# Height is skipped! I grabbed a lemonade. 

#BinaryTree -> boolean
# takes in a BinaryTree and returns true when a value n has a left or right of 3n
def has_triple(treeNode):
  if treeNode == "mt":
    return False
  elif treeNode.left == "mt" and treeNode.right == "mt":
    return False
  else:
    if treeNode.left != "mt":
      if treeNode.left.value == treeNode.value * 3:
        return True
    if treeNode.right != "mt":
      if treeNode.right.value == treeNode.value * 3:
        return True
    return has_triple(treeNode.left) or has_triple(treeNode.right)


#BinaryTree -> BinaryTree
# takes a BinaryTree and returns a new tree with all values smaller by one. 
def sub_one_map(treeNode):
  if (treeNode == "mt"):
    return 0
  else: 
    return TreeNode(treeNode.value - 1, sub_one_map(treeNode.left), sub_one_map(treeNode.right))

import unittest

class TestCase(unittest.TestCase):
  def test_size(self):
    treeNode = "mt"
    self.assertEqual(size(treeNode), 0)
    Node = TreeNode(3, TreeNode(2, "mt", "mt"), TreeNode(3, "mt", "mt"))
    self.assertEqual(size(Node), 3)

  def test_num_leaves(self):
    treeNode = "mt"
    self.assertEqual(num_leaves(treeNode), 0)
    Node = Node = TreeNode(3, TreeNode(2, "mt", TreeNode(3, "mt", "mt")), TreeNode(2, "mt", "mt"))
    self.assertEqual(num_leaves(Node), 2)

  def test_sum(self):
    treeNode = "mt"
    self.assertEqual(sum(treeNode), 0)
    Node = TreeNode(3, TreeNode(2, "mt", TreeNode(3, "mt", "mt")), TreeNode(2, "mt", "mt"))
    self.assertEqual(sum(Node), 10)

  def test_has_triple(self):
    treeNode = "mt"
    self.assertEqual(has_triple(treeNode), False)
    Node = TreeNode(3, TreeNode(2, "mt", TreeNode(3, "mt", "mt")), TreeNode(2, "mt", "mt"))
    self.assertEqual(has_triple(Node), False)
    node2 = TreeNode(3, TreeNode(9, "mt", "mt"), TreeNode(2, "mt", "mt"))
    self.assertEqual(has_triple(node2), True)

  def test_sub_one_map(self):
    treeNode = "mt"
    self.assertEqual(sub_one_map(treeNode), 0)
    Node = TreeNode(3, TreeNode(2, "mt", TreeNode(3, "mt", "mt")), TreeNode(2, "mt", "mt"))
    self.assertEqual(sub_one_map(Node), TreeNode(2, TreeNode(1, 0, TreeNode(2, 0, 0)), TreeNode(1, 0, 0)))

if (__name__ == '__main__'):
    unittest.main()
