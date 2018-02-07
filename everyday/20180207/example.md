# 集合的練習, python Set
集合的特性：
1. 元素不會重複，可利用其特性來進行去除重複元素
2. 可以進行集合運算，例如：交集、聯集及差集等等集合運算。
3. 與list, dict, tuple都不同，set是無序的列的組合，因此無法用索引存取，但仍然可以用for進行迭代運算。

* 練習範例： https://repl.it/@Traveler/Python-Set


```python
# Use dict to show simple case.
dict_one = {1: None, 2: None, 5: None, 2: None}
# set(dict_one) => {1, 2, 5}, delete the duplicate element.
dict_two = {1: None, 2: None, 3: None}
# If you wnat to get the difference between dict_one and dict_two, you can use set method.

# difference(差集)
difference = set(dict_one) - set(dict_two)
print('difference', difference)

# intersection(交集)
intersection = set(dict_one) & set(dict_two)
print('intersection', intersection)

# union(聯集)
union = set(dict_one) | set(dict_two)
print('union', union)

# symmetric_difference(對稱差)
symmetric_difference = set(dict_one) ^ set(dict_two)
print('symmetric_difference', symmetric_difference)

parent_set = set([1, 2, 3, 4, 5])
sub_set = set([1, 2])
# sub set
if sub_set.issubset(parent_set):
    print("sub_set is a parent_set's sub set.")
else:
    print("sub_set isn't a parent_set's sub set.")

# super set
if parent_set.issuperset(sub_set):
    print("parent_set is a sub_set's super set.")
else:
    print("parent_set isn't a sub_set's super set.")

```
