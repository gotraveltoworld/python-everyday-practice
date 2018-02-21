# Python collections extend

### collections extend:
1. namedtuple(): Generate sub-tuple that can access by name.
2. deque(double-ended queue): The kind of queue that can access by two head.
    - Methods: .popleft(), .appendleft()
    - Reference: (deque, rotate())https://stackoverflow.com/questions/8458244/swap-letters-in-a-string-in-python
3. Counter: To generate the histogram graph.
4. OrderedDict: Sequence dictionary.
5. defaultdict: The dictionary has a default value.

練習範例：https://repl.it/@Traveler/Python-collections-extend
```python
# 本範例是參考以下網址自行練習python collections中的一些方法
# Reference: http://www.zlovezl.cn/articles/collections-in-python/
"""Collections methods.
    collections extend:
        1. namedtuple(): Generate sub-tuple that can access by name.
        2. deque(double-ended queue): The kind of queue that can access by two head.
            - Methods: .popleft(), .appendleft()
            - Reference: (deque, rotate())https://stackoverflow.com/questions/8458244/swap-letters-in-a-string-in-python
        3. Counter: To generate the histogram graph.
        4. OrderedDict: Sequence dictionary.
        5. defaultdict: The dictionary has a default value.
"""
# namedtuple: 參照先前的練習紀錄, https://repl.it/@Traveler/Python-Names-of-tuple
# deque:
"""deque area, 若需要使用它，最主要是降低時間複雜度：
    * list複雜度O(n)
    * deque複雜度O(1)
"""
from collections import deque

queue = deque(['Qoo', '-----', '----', '!!!'])
for i in range(4):
    queue.rotate(1) # 往右邊移動一格，當到底端時會重新回到原點。
    print(queue)
"""Result
    deque(['!!!', 'Qoo', '-----', '----'])
    deque(['----', '!!!', 'Qoo', '-----'])
    deque(['-----', '----', '!!!', 'Qoo'])
    deque(['Qoo', '-----', '----', '!!!'])
"""
# Counter: 參照先前的練習紀錄, https://repl.it/@Traveler/Python-Counter
# OrderedDict:
"""OrderedDict area.
    用A, B, C三個鍵值測試，OrderedDict會根據元素順序排序。
    因為有排序，因此兩個dict會被歸類成不同對象。
"""
from collections import OrderedDict

item1 = {
    'A': 1,
    'B': 2,
    'C': 3
}
item2 = {
    'A': 1,
    'C': 3,
    'B': 2
}
# Normal
regular_dict1 = item1
regular_dict2 = item2
print(regular_dict1, regular_dict2)
if regular_dict1 == regular_dict2:
    print('OK')
else:
    print('Bye')

# OrderedDict
regular_dict1 = OrderedDict(item1)
regular_dict2 = OrderedDict(item2)
print(regular_dict1, regular_dict2)
if regular_dict1 == regular_dict2:
    print('OK')
else:
    print('Bye')

"""
{'A': 1, 'B': 2, 'C': 3} {'A': 1, 'C': 3, 'B': 2}
OK
OrderedDict([('A', 1), ('B', 2), ('C', 3)])
OrderedDict([('A', 1), ('C', 3), ('B', 2)])
Bye
Bye
"""
```
