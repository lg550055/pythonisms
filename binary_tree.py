class BinaryTree:

    def __init__(self, collection=None):
        self.root = None
        self.length = 0
        if collection:
            for item in collection: # [a,b,c] => Root-> [a], [b], [c], end
                self.insert(item)
                self.length += 1

    def __iter__(self):
        def value_generator():
            q = [self.root]
            while q:
                current = q.pop(0)
                yield current.value
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return value_generator()

    def __str__(self):
        out = "Root-> "
        for value in self:
            out += f"[{value}], "
        return out + "end"

    def __len__(self):
        return self.length

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        return list(self)[index]

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return
        q = [self.root]
        while q:
            current = q.pop(0)
            if current.left is None:
                current.left = node
                return
            if current.right is None:
                current.right = node
                return
            q.append(current.left)
            q.append(current.right)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
