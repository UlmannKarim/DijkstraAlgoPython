# KARIM ABDUL ULMANN 119329701

class Element:  # to start with the APQ we first make an element class
    """ A key, value and index. """

    def __init__(self, k, v, i):
        self._key = k  # priority
        self._value = v  # value stored
        self._index = i  # index in array

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def getIndex(self):
        return self._index

    def getValue(self):
        return self._value

    def getKey(self):
        return self._key

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None

    def __str__(self):
        ans = 'Key:' + str(self._key) + '  Value:' + str(self._value) + '  Index:' + str(self._index)
        return ans


class APQ:  # the APQ will have instances of the element class as nodes in the Binary Heap

    def __init__(self):
        self._Bheap = []
        self._size = 0
        # self._root = self._Bheap[0]

    # NOTE
    # whenever we swap two elements in the heap
    # (during a swap or a bubble up or bubble down)
    # we must update the _index attributes in the Elements.

    def add(self, key, item):
        # add a new item into the priority queue with priority key,
        # and return its Element in the APQ
        # -create the Element with index of last place,
        # add to heap and bubble up, changing indices of Elts,
        # return the Element
        newIndex = len(self._Bheap)  # should we add plus 1?
        newElement = Element(key, item, newIndex)
        self._Bheap.append(newElement)
        self._size += 1
        # check if is in right place
        # bubble up--
        self.bubbleup(newElement._index)
        return newElement

    # bubbling up does work! :)

    def min(self):  # read root element
        if self._size == 0:
            return None
        return self._Bheap[0]

    def remove_min(self):
        # - swap first element into last place,
        # pop the element,
        # bubble top element down,
        # changing indices, return popped
        # key,value

        if self._size == 0:
            return None

        self._Bheap[0], self._Bheap[-1] = self._Bheap[-1], self._Bheap[0]
        self._Bheap[-1]._index, self._Bheap[0]._index = self._Bheap[0]._index, self._Bheap[-1]._index

        topper = self._Bheap.pop()
        self._size -= 1
        if self._size == 0:  # if APQ is now empty
            return topper

        self.bubbledown(self._Bheap[0]._index)
        return topper

    def update_key(self, element, newkey):
        element._key = newkey
        parent = self.getParent(element)
        if parent is None:
            pass
        elif parent._key > element._key:
            self.bubbleup(element._index)
        else:
            self.bubbledown(element._index)

    def get_key(self, element):
        return element._key

    def remove(self, element):
        # remove the element from the APQ,
        # and rebalance APQ-update the element's key,
        # if key less than parent's key, bubble up;
        # else bubble down, while changing indices

        if element not in self._Bheap:
            print('Element Does Not Exist!')
        else:

            root = self._Bheap[0]
            if element == root:
                self.remove_min()

            else:
                newest = self._Bheap[self._size - 1]
                eleIndex = element._index
                self._Bheap[eleIndex] = newest
                self._Bheap.pop(self._size - 1)  # pop last copy
                self._size -= 1  # shrink size of heap
                self._Bheap[eleIndex]._index = eleIndex  # set new index
                replacement = self._Bheap[eleIndex]
                parent = self.getParent(replacement)

                # print(replacement)
                # print(parent)

                # if key less than parent's key, bubble up;
                # else bubble down, while changing indices
                if element._key < parent._key:
                    self.bubbleup(element)
                else:
                    self.bubbledown(element._index)

    def getParent(self, element):
        # returns the parent of the element given, return None if it's the root
        root = self._Bheap[0]
        if root == element:
            return None
        else:
            parent = self._Bheap[(element._index - 1) // 2]
            return parent

    def bubbleup(self, index):
        element = self._Bheap[index]

        while index > 0:  # while parent is not the root
            parent = (index - 1) // 2

            if self.get_key(element) < self._Bheap[parent]._key:
                # print('swapping:', inlist[i], 'with its parent:', inlist[parent])
                self._Bheap[element._index], self._Bheap[parent] = \
                    self._Bheap[parent], self._Bheap[element._index]  # swap positions
                self._Bheap[element._index]._index, self._Bheap[parent]._index = \
                    self._Bheap[parent]._index, self._Bheap[element._index]._index  # swap ._indexes
                index = parent
            else:
                index = 0

    def bubbledown(self, index):
        last = self._Bheap[-1]._index

        while last > (index * 2):
            # use index first
            lc = index * 2 + 1
            rc = index * 2 + 2
            miniChild = lc  # assume that the minimum child is left first

            if last > lc and self._Bheap[rc]._key < self._Bheap[lc]._key:  # rc exists and is bigger
                miniChild = rc

            if self._Bheap[index]._key > self._Bheap[miniChild]._key:
                self._Bheap[index], self._Bheap[miniChild] = self._Bheap[miniChild], self._Bheap[
                    index]  # flip positions
                self._Bheap[miniChild]._index, self._Bheap[index]._index = self._Bheap[index]._index, self._Bheap[
                    miniChild]._index  # flip indexes!
                index = miniChild

            else:
                index = miniChild

    def __str__(self):
        ans = ''
        for elemnt in self._Bheap:
            ans += str(elemnt) + ', '
        return ans
