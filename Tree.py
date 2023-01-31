class Tree:

    class Position:

        def element (self):

            raise NotImplementedError('must be implemend by subclass')
        def __eq__(self,other):

            raise NotImplementedError("must be implemented by subclass")
        def __ne__(self,other):

            return not(self==other)
            raise NotImplementedError("must be implemented by subclass")

    def root(self):

        raise NotImplementedError("must be implemented by subclass")

    def parent (self,p):

        raise NotImplementedError("must be implemented by subclass")

    def num_children(self,p):

        raise NotImplementedError("must be implemented by subclass")
    def children(self,p):

        raise NotImplementedError("must be implemented by subclass")
    def __len__(self):

        raise NotImplementedError("must be implemented by subclass")

    def is_empty(self):
        return len(self) == 0


class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError('must be implemented by subclas')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclas')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)



class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    def add(self, val):
        if self.is_empty():
            return self._add_root(val)
        else:
            return self._help_add(val, self.root())

    def _help_add(self, val, p):
        node = self._validate(p)
        if val < node._element:
            if node._left is None:
                return self._add_left(p, val)
            else:
                return self._help_add(val, self._make_position(node._left))
        else:
            if node._right is None:
                return self._add_right(p, val)
            else:
                return self._help_add(val, self._make_position(node._right))
    def _add_root(self, val):
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(val)
        return self._make_position(self._root)

    def _add_left(self, p, val):
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exists')
        node._left = self._Node(val, node)
        self._size += 1
        return self._make_position(node._left)

    def _add_right(self, p, val):
        node = self._validate(p)
        if node._right is not None: raise ValueError('Right child exists')
        node._right = self._Node(val, node)
        self._size += 1
        return self._make_position(node._right)

    def _replace(self, p, val):
        node = self._validate(p)
        old = node._element
        node._element = val
        return old

if __name__ == '__main__':
    t = LinkedBinaryTree()
    t.add(15)
    t.add(8)
    t.add(18)
    t.add(27)
    t.add(19)
    t.add(5)
    t.add(2)
    t.add(11)
    t.add(17)

    p1 = t.add(47)
    p2 = t.add(55)
    t._replace(t.right(p1),60) # I can't add to the right because it has right .So I am gonna replace it u can test it !
    t._add_left(p1, 25)

