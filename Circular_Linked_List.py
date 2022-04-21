class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Circular_Linked_List:
    def __init__(self):
        self.head = None

    def __repr__(self):
        current = self.head
        list = ''
        while current:
            list += str(current.value)
            list += ' '
            current = current.next
            if current == self.head:
                break
        return list

    def append_node(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.head.next = self.head

        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head

    def make_list_from_list(self, note):

        formula = [2, 4, 5, 7, 9, 11]
        temp_formula = list(formula)
        scale = Circular_Linked_List()
        scale.append_node(note)

        start = None
        current = self.head
        while not start:
            current = current.next
            if type(current.value) == list:
                if note in current.value:
                    start = current.value
            else:
                if note == current.value:
                    start = current.value
        counter = 0
        while len(temp_formula) != 0:
            while counter != temp_formula[0]:
                temp_prev = current
                current = current.next
                counter += 1
            if type(current.value) == list:
                if temp_prev.value not in current.value[0]:
                    scale.append_node(current.value[1])
                else:
                    scale.append_node(current.value[0])
            else:
                scale.append_node(current.value)
            temp_formula.pop(0)


        return scale












        return start






    # def prepend_node(self, value):
    #     new_node = Node(value)

    #     if not self.head:
    #         self.head = new_node
    #         self.head.next = self.head

    #     else:
    #         current = self.head
    #         while current.next != self.head:
    #             current = current.next
    #         current.next = new_node
    #         new_node.next = self.head
    #         self.head = new_node
