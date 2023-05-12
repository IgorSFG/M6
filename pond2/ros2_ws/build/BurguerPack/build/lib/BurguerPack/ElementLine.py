# Código feito em sala de aula
class ElementLine():
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Line():
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
        else:
            out_value = self.head.value
            self.head = self.head.next
            self.size -= 1
            print(out_value)


    def __repr__(self) -> str:
        if self.head is None:
            return "Line -> None"
        return f"Line -> {self.head.value}"