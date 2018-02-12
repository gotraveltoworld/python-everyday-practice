# Python named of tuple method.
* 生成可以用名稱存取的tuple
* 練習範例： https://repl.it/@Traveler/Python-Names-of-tuple
* 參考：[相關說明](http://kodango.com/understand-defaultdict-in-python)

```python
# If you use class to print some transform format.
class Example:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def __str__(self):
        # string templat: http://www.cnblogs.com/vamei/archive/2013/03/12/2954938.html
        return '(%g, %g)' % (self.a, self.b)

ex = Example(1, 2)
print(ex)

# named tuple module.
from collections import namedtuple
# Set Eample object has a and b attribute.
Example = namedtuple('Example', ['a', 'b'])
print(Example)

# Use Point just like function, Point(a=1, b=2)
ex = Example(a=1, b=2)
print('p.a:', ex.a, 'p.b', ex.b)
print('attribute:', ex.a, ex.b)
print('list format:', ex[0], ex[1])
a, b = ex
print('a,b:', a, b)
```
