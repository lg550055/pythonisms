import pytest
from binary_tree import BinaryTree


def test_exists():
  assert BinaryTree


def test_build_tree():
  tree = BinaryTree(['a','b','c'])
  assert str(tree) == 'Root-> [a], [b], [c], end'


def test_build_longer_tree():
  tree = BinaryTree(['a','b','c','d','e'])
  assert str(tree) == 'Root-> [a], [b], [c], [d], [e], end'


def test_build_tree_len():
  tree = BinaryTree(['a','b','c'])
  assert len(tree) == 3


def test_get_item():
  tree = BinaryTree(['a','b','c'])
  assert tree[1] == 'b'


def test_get_item_out_of_range():
  tree = BinaryTree(['a','b','c'])
  with pytest.raises(IndexError):
    tree[10]


def test_get_item_neg_index():
  tree = BinaryTree(['a','b','c'])
  with pytest.raises(IndexError):
    tree[-1]


def test_equals():
  tree1 = BinaryTree(['a','b','c'])
  tree2 = BinaryTree(['a','b','c'])
  assert tree1 == tree2


def test_not_equals():
  tree1 = BinaryTree(['a','b','c'])
  tree2 = BinaryTree(['c','b','a'])
  assert len(tree1) == len(tree2)
  assert tree1 != tree2


def test_list_comprehension():
  tree = BinaryTree([1,2,3,4,5])
  lc = [n for n in tree if n>2]
  assert lc == [3,4,5]


def test_truthy():
  tree = BinaryTree([1,2,3,4,5])
  assert tree
