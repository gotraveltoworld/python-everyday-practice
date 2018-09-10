# Python property function of class.

## 前言
練習`property`語法和說明其用法，[參照]。(!https://openhome.cc/Gossip/Python/Property.html)

```python
# 範例：
class Ball:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('必須是正數')
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError('必須是正數')
        self.__radius = radius

    def del_radius(self, radius):
        del self.__radius

# 直接使用property()取用
radius = property(get_radius, set_radius, del_radius, 'radius 特性說明')
# 使用方法就像是使用類別屬性一樣。
ball = Ball(1.23)
print(ball.radius)
ball.radius = 2.31
```
改成另外一種形式：`@property`關鍵字，裝飾器(decorator)
```python
class Ball:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('必須是正數')
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @radius.deleter
    def radius(self):
        del self.__radius
```
本篇純粹範例，需要理解`decorator`的概念，才能更清楚程式如何運作。