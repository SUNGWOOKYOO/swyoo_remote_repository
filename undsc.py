class undsc:
    def __init__(self):
        self._x = 10
        self.__y = 10

    def func1(self):
        print("public func! ")
    
    def _func2(self):
        print("one underscore func! ")

    def __func3(self):
        print("two underscore func! ")
        
    def gety(self):
        return self.__y
    
    def getfunc3(self):
        self.__func3()

if __name__ == "__main__":
    obj = undsc()
    print(obj._x,": _x")
    #print(obj.__y)

    obj.func1()
    obj._func2()
    #obj.__func3()

    print(obj.gety(),": __y")
    print(obj.getfunc3(),": use __func3")
else:
    print("This part can be showed when only being imported ")