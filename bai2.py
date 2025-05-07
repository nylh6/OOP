import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        x, y = map(int, input("Nhập tọa độ x y: ").split())
        self.__x = x
        self.__y = y

    def print(self):
        print(f"({self.__x}, {self.__y})")

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distance(self, other):
        return math.hypot(self.__x - other.__x, self.__y - other.__y)


class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 2:
            if not (isinstance(args[0], Point) and isinstance(args[1], Point)):
                raise TypeError("Nhập điểm!!!")
            self.__d1 = args[0]
            self.__d2 = args[1]
        elif len(args) == 4:
            if not all(isinstance(item, int) for item in args):
                raise TypeError("Only Integers can be added")
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        elif len(args) == 1:
            if not isinstance(args[0], LineSegment):
                raise TypeError("Only one LineSegment can be added")
            self.__d1 = Point(args[0].__d1.getX(), args[0].__d1.getY())
            self.__d2 = Point(args[0].__d2.getX(), args[0].__d2.getY())

    def read(self):
        s = input("Nhập vào đoạn thẳng:")
        self.__d1 = Point(int(s.split()[0]), int(s.split()[1]))
        self.__d2 = Point(int(s.split()[2]), int(s.split()[3]))

    def __str__(self):
        return "(({}, {}), ({}, {}))".format(
            self.__d1.getX(), self.__d1.getY(),
            self.__d2.getX(), self.__d2.getY()
        )

    def move(self, dx, dy):
        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)

    def length(self):
        return self.__d1.distance(self.__d2)

    def angle(self):
        return int(math.atan2(
            self.__d2.getY() - self.__d1.getY(),
            self.__d2.getX() - self.__d1.getX()
        ))


class LineSegmentTest:
    def testCase1(self):
        A = Point(2, 5)
        B = Point(20, 35)
        AB = LineSegment(A, B)
        print(AB)
        AB.move(35, 51)
        print(AB)

    def testCase2(self):
        CD = LineSegment()
        print("|CD| = {:.2f}".format(CD.length()))

    def testCase3(self):
        danhsach = []
        n = int(input("Nhập n: "))
        for i in range(n):
            l1 = LineSegment()
            l1.read()
            danhsach.append(l1)

        print("Danh sách ban đầu:")
        for item in danhsach:
            print(item)
            print(item.length())

        danhsach.sort(key=lambda dist: dist.length())
        print("Danh sách sau khi sắp xếp theo độ dài:")
        for item in danhsach:
            print(item)
            print(item.length())

    def main(self):
        while True:
            s = input("nhập kịch bản muốn chạy 1/2/3/exit: ")
            if s == '1':
                self.testCase1()
            elif s == '2':
                self.testCase2()
            elif s == '3':
                self.testCase3()
            elif s == 'exit':
                break

LineSegmentTest().main()

