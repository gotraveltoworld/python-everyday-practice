class ParentClass:
    def show(self):
        print('Parent')

class ChildClass(ParentClass):
    def parent_show(self):
        super().show()
    def show(self):
        print('Child')

ChildClass().parent_show() # Parent
ChildClass().show() # Child


class ShowEncapsulation:
    __name = 'private_name'
    _name = 'protest_name'
    name = 'public_name'
    pass

print(ShowEncapsulation().name)
print(ShowEncapsulation()._name)
try:
    print(ShowEncapsulation().__name)
except Exception as e:
    print(e) #'ShowEncapsulation' object has no attribute '__name'

# To enforce to get the function of private.
print(ShowEncapsulation()._ShowEncapsulation__name) # private_name


# Print the object
class PrintObj:
    __origin = 0
    __after = 0
    __str = 'Show...!'

    def __init__(self, origin, after):  # Initial
        self.__origin = origin
        self.__after = after

    def __str__(self):
        return (self.__str)

    def __add__(self, other):
        return (self.__origin + other.__after)
# https://openhome.cc/Gossip/Python/SpecialMethodNames.html
c1 = PrintObj(1, 9)
c2 = PrintObj(1, 9)
print(c1 + c2)