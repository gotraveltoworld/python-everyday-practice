# Python dict預設值相關的方法，(setdefault & defaultdict)
* 練習範例： https://repl.it/@Traveler/Python-Counter
* 參考1：[相關說明1](http://kodango.com/understand-defaultdict-in-python)
* 參考2：[相關說明2](http://code.activestate.com/recipes/523034/)
1. 基本上dict的格式，但是存取不存在的索引值時，會即時回傳一個值。
2. 都是處理key值不存在時可以透過這個方式存取預設值。

```python
# Generate a dict
words = ('apple', 'kiwi', 'pineapple', 'strawberry',
           'buleberry', 'redberry', 'redberry', 'kiwi')
counts = {}
for word in words:
    counts.setdefault(word, 0)
    counts[word] += 1
print(counts)
# {'apple': 1, 'kiwi': 2, 'pineapple': 1, 'strawberry': 1, 'buleberry': 1, 'redberry': 2}
```


defaultdict
1. 使用方法要引入`from collections import defaultdict`。
2. 原始的dict設定預設值，本身就提供預設值
* defaultdict初始化傳入一個類型作為參數，當存取的鍵值不存在，就會回傳預設的類型資料。

```python
from collections import defaultdict

dic = defaultdict(list)
val = dic['key']
print(val)
val.append('bye')
print(dic)
# defaultdict(<class 'list'>, {'key': ['bye']})
```
* 這種類型的預設值只能用`dict[key]`或者`dict.__getitem__(key)`存取才會有效。

```python
from collections import defaultdict

test = defaultdict(list)
# Error, if you use the illegal method to access.
print(test.append('other_key'))
# Traceback (most recent call last):
#  File "python", line 21, in <module>
# AttributeError:  'collections.defaultdict' #object has no  attribute 'append'

# legal method.
print(test.get('something'))
print(test['something'])

```
defaultdict也可以用一般函式來產生預設值。
```python
from collections import defaultdict

def folat_one():
    return 1.0

dic = defaultdict(folat_one)
print(dic['one_key'])
# 1.0

# Use lambda
dic = defaultdict(lambda : 1.0)
print(dic['lamda_key'])
# 1.0
```
以下是defaultdict實現的方式的一些說明：
1. python 2.5以上支援dict中的`__missing_＿`方法，所以當存取不存在的鍵值時就會使用`__missing__`方法來回傳預設值。
2. dict本身支援`__missing__`方法，但是其本身不存在這個方法。
```python
# pyhon 3.6.1
# Print all dict method (print(dir(dict))
'__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# About __missing__ method
# Reference : https://docs.python.org/3/library/stdtypes.html#dict
print((defaultdict.__missing__.__doc__))


# Implement the __missing__
class DefaultValue(dict):
    def __missing__(self, key):
        self[key] = 'default'
        return 'default'
dic = DefaultValue()
print(dic['key'])
dic['key'] = 'Bye'
print(dic['key'])
```

其他版本實現的範例如下：
[參照](http://code.activestate.com/recipes/523034/)
