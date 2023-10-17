class swift():
    def gear(self):
        print("the car with 5 gear")
    def color(self):
        print("red")
class i20(swift):
    def gear1(self):
        print("the car with 6 gear")
    def color1(self):
        print("blue")
    def func(obj):
        obj.gear()
        obj.gear1()
obj=swift()
obj2=i20()
obj2.func()
obj.color()
obj2.color1()
