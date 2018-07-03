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