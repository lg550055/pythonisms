# Lab 42 - Pythonisms

### Iterators, generators and dunder methods

Created a class Binary Tree with the following methods:

- `__init__`
  - accepts a collection of values and creates a bianry tree using the `insert` method
  - has a `length` attribute
  - has a `root` attribute

- `__iter__`
  - uses a generator to allow iterating through the tree, which facilitates using the tree in list comprehensions and casting the tree as a list

- `__str__`
  - creates a string representation fo the tree in the form `Root-> [a], [b], [c], end`

- `__len__`
  - returns the length of the tree in O(1)

- `__eq__`
  - ascertains wheather one tree is equal to another

- `__getitem__`
  - given an zero-based index, i, returns the value of ith element of the tree

- `insert`
  - given a value, appends a node with the value to the first available possition in the tree, keeping the tree as balanced as possible

### Decorators

