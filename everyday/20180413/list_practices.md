# Python lists practice.

## Practices
1. 10-1: 處理nested list, 加總全部元素
```python
def nested_sum(array):
    return [sum(a) if type(a) == list else a for a in array if a]
    # [[1, 3], 2] => [4, 2]
```
2. 10-2: 累計(cumulative sum)加總list, 回傳一個新的list, 內容中每個元素會是原本list中`i + 1`的總和。
```python
def cumsum(array):
    return [sum(array[0:index]) for val, index in enumerate(array)]
    # [1, 2, 3] => [1, 3, 6]
```
3. 10-3: middle, 回傳新的list, 其中含有原始list除了第一個和最後一個元素。
```python
def middle(array):
    return array[1:-1]
    # [1, 2, 3, 4, 5] => [2, 3, 4]
```
4. 10-4: chop, 移除第一個和最後一個元素, 回傳None。
```python
def chop(array):
    array.pop(0)
    array.pop(-1)
    return None
    # [1, 2, 3, 4, 5] => [2, 3, 4]
```
5. 10-5: is_sorted, 判斷該list是否是遞增順序(ascending order)，是的話回傳`True`，否的話回傳`False`。
```python
def is_sorted(array):
    previous = 0
    for a in array:
        if previous > a:
            return False
        else:
            previous = a
    return True
```
6. 10-6: is_anagram, 是否是易位構詞(anagram), for example: stop and post
* You can use the set to filter the value of duplicate.
```python
def is_anagram(word1, word2):
    return set(word1) == set(word2) and len(word1) == len(word2)
```
7. 10-7: has_duplicates, 接收一個串列，判斷是否有重複的值，是的話回傳`True`，否的話回傳`False`。
```python
from collections import Counter
def has_duplicates(array):
   return  any(int(r) > 1 for r in [v for v in Counter(array).values()])
```
8. 10-8: birthday_paradox, 生日問題
* Link: https://repl.it/@Traveler/listsfunctions
```python
# https://zh.wikipedia.org/wiki/%E9%9A%8E%E4%B9%98
def count_factorial(n):
    sum = 1
    total = 0
    for i in range(1, n+1):
        sum *= i
        total += sum
    return total
# https://zh.wikipedia.org/wiki/%E7%94%9F%E6%97%A5%E5%95%8F%E9%A1%8C
def birthday_paradox(n = 23):
    return 1 - (count_factorial(365) / ((365 ** n) * counts_n(365 - n)))
```
9. 10-9: Count the results, 用兩種方式串階list。
```python
    start = time.time()
    list_data = []
    for w in load_words():
        list_data.append(w)
    print('append time:', time.time() - start)

    list_data = []
    start = time.time()
    for w in load_words():
        list_data += [w]
    print('[] + [] time:', time.time() - start)
```
10. 10-10:
要檢查一個字是否在字彙表(word list)上，可以用`in`運算子，但是 __速度會比較慢__ ，因為是用有序的方式搜尋。
採用`bisect`二分搜尋的方式來優化。
* [bisect(python doc)](https://docs.python.org/3.5/library/bisect.html#module-bisect)
* [other 1](http://kuanghy.github.io/2016/06/14/python-bisect)
* [other 2](https://www.cnblogs.com/skydesign/archive/2011/09/02/2163592.html)

```python
# To look up a letter grade for an exam score (say) based on a set of ordered numeric breakpoints.
# This is a office example.
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]
# [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
# ['F', 'A', 'C', 'C', 'B', 'A', 'A']

from bisect import bisect

def in_bisect(sorted_list, target_value):
    i = bisect(sorted_list, target_value)
    return i

sorted_list = [2, 3, 8, 1, 0, -1]
print(sorted(sorted_list)) # Ensure the orderd list.
print(in_bisect(sorted(sorted_list), 4))
# [-1, 0, 1, 2, 3, 8]
# 5 (回傳預定插入的索引)
```

11. 10-11:
判斷兩個list是否為反向的存在，可以參考字串的做法。
```python
def is_reverse(list1, list2):
    # Guardian pattern.
    if len(list1) != len(list2):
        return False

    i = 1
    for w1 in list1:
        if w1 != list2[-i]:
            return False
        i += 1
    return True
```
