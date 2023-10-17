class base:
    def __init__(self):
        self.a="python"
        self.__c="django"
class derived(base):
    def __init__(self):
        base.__init__(self)
        print("studing")
        print(self.__c)
obj=base()
print(obj.a)
obj1=drived()

