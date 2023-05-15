# Código feito em sala de aula
class ElementLine:
    def __init__(self, value, next_element=None):
        self.value = value
        self.next = next_element

class Line:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, x):
        new_element = ElementLine(x, None)
        if self.head is None:
            self.head = new_element
            self.tail = self.head
        else:
            self.tail.next = new_element
            self.tail = self.tail.next
        self.size += 1

    def pop(self):
        if self.head is None:
            print("Line is empty")
            return None
        else:
            out_value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return out_value

    def __repr__(self):
        elements = []
        current_element = self.head
        while current_element is not None:
            elements.append(str(current_element.value))
            current_element = current_element.next
        if len(elements) == 0:
            return "Line -> None"
        else:
            return "Line -> " + " -> ".join(elements)
