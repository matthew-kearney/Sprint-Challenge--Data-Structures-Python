class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # for node empty
        if node is None:  
             return

        # to get to end of the SLL
        if node.get_next() is None:
            # set tail to head of RL
            self.head = node 
            return

        # RL by converting current node with pervious node (recursive)
        self.reverse_list(node.get_next(), node)
        # set value of the second value in orginal list to be the second to last in new node
        node.get_next().set_next(node)
        # set next value to be none on new tail
        node.set_next(None) 
