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

