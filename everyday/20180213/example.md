# Python Class基本語法

基本定義：
1. Class：類別
2. Instance：實體
3. Attribute：類別屬性

練習：https://repl.it/@Traveler/Python-Class-example
```python
class DemoClass:
    """Demo the basic class"""
    __x = 0 # Attribute x
    __y = 0 # Attribute y

    # Initial the class.
    def __init__(self, x=0, y=0):

        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

demo = DemoClass(10, 20)
print('x:', demo.get_x()) # 10
print('y:', demo.get_y()) # 20

print(type(demo)) # <class 'DemoClass'>
print(isinstance(demo, DemoClass)) # True
print(hasattr(demo, 'get_x')) # True
print(hasattr(demo, 'get_y')) # True
print(hasattr(demo, 'get_z')) # False

try:
    demo.get_z()
except AttributeError as attr:
    print(attr) # 'DemoClass' object has no attribute 'get_z'
```