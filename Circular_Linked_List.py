
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None



class Circular_Linked_List:
    # Implementation of a classic data structure Circular_Linked_List
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
            self.head.prev = self.head

        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node

    def check_last(self):
        return self.head.prev

    def generating_list(self, formula=None):
    # Generate a list from a looped list of tones according to chord formula.
        temp_formula = list(formula)
        ret_list = []
        current = self.head
        while current:
            ret_list.append(current.value + ' ' + temp_formula[0])
            temp_formula.pop(0)
            current = current.next
            if current == self.head:
                break

        return ret_list


    def gen_pure_list(self):
        # Flattening Circular_Linked_List to a regular python list
        list_to_return = []
        current = self.head
        while current:
            list_to_return.append(current.value)
            current = current.next
            if current == self.head:
                break
        return list_to_return



    def make_list_from_list(self, note, formula, mode='normal'): 
        # Generate a list from a looped list of tones according to scale formula.
        temp_formula = list(formula)
        ret_list = Circular_Linked_List()
        ret_list.append_node(note)

        start = None
        current = self.head
        while not start:
            current = current.next
            if type(current.value) == list:
                if note in current.value:
                    start = current.value
            else:
                if note == current.value:
                    start = current

        counter = 0
        while len(temp_formula) != 0:
            while counter != temp_formula[0]:
                current = current.next
                counter += 1
            if type(current.value) == list:
                if mode == 'normal':
                    first = 1
                    second = 0
                else:
                    first = 0
                    second = 1

                if ret_list.check_last().value[0] == current.value[0][0]:
                    ret_list.append_node(current.value[first])
                else:
                    ret_list.append_node(current.value[second])
                
            else:
                ret_list.append_node(current.value)

            temp_formula.pop(0)

        return ret_list


