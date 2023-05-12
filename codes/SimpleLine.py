class Line(list):
    def __init__(self, points):
        super().__init__(points)

    def push(self, x):
        return super().append(x)
    
    def pop(self):
        return super().pop(0)
    
    def __repr__(self):
        return f"Line -> {super().__repr__()}"

def main():
    line = Line([1,2,3,4])
    print(line)
    line.push(5)
    print(line)
    line.pop()
    print(line)


if __name__ == '__main__':
    main()