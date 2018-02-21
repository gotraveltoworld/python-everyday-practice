# Python Class 一些相關用法

1. 類別的內嵌
    - 用類別屬性指向外部類別
    - 可用不同類別的方法
2. 物件的複製
    - Shallow copy
    - Deep copy

練習：https://repl.it/@Traveler/Python-Class-example-2
```python
import copy

class DemoClassSub:
    """Sub Demo class."""
    a = 11
    b = 22

    def __init__(self, a=11, b=22):
        self.a = a
        self.b = b

    def get_ab(self):
        return self.a, self.b

class DemoClass:
    """Demo the basic class"""
    __x = 0 # Attribute x
    __y = 0 # Attribute y

    # Initial the class.
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_x(self, x=0):
        self.__x = x

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

d = DemoClass()
d.sub_class = DemoClassSub() # Set the other class.
d_cpoy = copy.copy(d)
d_cpoy_deep = copy.deepcopy(d)
# Add some data
d.set_x(111)
print(d.get_x()) # 111
print(d_cpoy.get_x()) # 0, shallow copy
print(d_cpoy_deep.get_x()) # 0, deep copy

# Shallow copy.
d.sub_class.a = 100
print(d.sub_class.a) # 100
print(d_cpoy.sub_class.a) # 100

# Deep copy
print(d_cpoy_deep.sub_class.a) # 11
```