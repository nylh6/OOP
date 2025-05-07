from bai1 import Point  

class ColorPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__()           
            self.__color = "xanh"
        elif len(args) == 3:
            x, y, color = args
            super().__init__(x, y)        
            self.__color = color
        elif len(args) == 1 and isinstance(args[0], ColorPoint):
            cp = args[0]
            super().__init__(cp.getX(), cp.getY())
            self.__color = cp.getColor()  
        else:
            raise ValueError("Invalid constructor arguments")

    def read(self):
        parts = input().split()
        x, y = int(parts[0]), int(parts[1])
        self.setXY(x, y)
        self.__color = parts[2]

    def print(self):
        print(f"({self.getX()}, {self.getY()}): {self.__color}")

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

class C002454:
    def testCase1(self):
        a = ColorPoint(5, 10, "trắng")
        a.print()

    def testCase2(self):
        b = ColorPoint()
        b.read()
        b.move(10, 8)
        b.print()

    def testCase3(self):
        c = ColorPoint(6, 3, "đen")
        d = ColorPoint(c)
        d.print()

        d.setColor("vàng")
        d.print()

        c.print()

    def main(self):
        self.testCase1()
        self.testCase2()
        self.testCase3()

if __name__ == "__main__":
    C002454().main()

