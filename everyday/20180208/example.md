# Python Counter 計數器的使用
1. 數學上定義的multiset，參照: [__wiki__](https://en.wikipedia.org/wiki/Multiset)
2. 類似集合，但是允許重複元素存在
```
 set = {a, b}
 multiset = {a, a, b}
```
3. 沒有序列的概念:
```
{a, a, b} = {b, a, a}
```
4. 用於統計單一文字各個字元的數量，可用於繪製__直方圖__。

* 練習範例： https://repl.it/@Traveler/Python-Counter


```python
# Need to import collections
from collections import Counter
text = 'This is a aplle.'
count = Counter(text)
print(count)
# Counter({' ': 3, 'i': 2, 's': 2, 'a': 2, 'l': 2, 'T': 1, 'h': 1, 'p': 1, 'e': 1, '.': 1})
# Count all char number.

# Base on an array.
arr = [1, 1, 2, 3, 4, 5, 0, 1, 2, 3, 5, 9]
count = Counter(arr)
print(count)
# Counter({1: 3, 2: 2, 3: 2, 5: 2, 4: 1, 0: 1, 9: 1})

# If you need to calculate all elements count you can use 'counter' to analytics.
```
### For example:
計算易位構詞(anagrams)：[易位構詞](https://cdlearth.wordpress.com/2010/05/03/anagram/)
```python
def anagrams(w1, w2):
    return len(Counter(w1)) == len(Counter(w2))

# anagrams('time', 'mint') == True
```
### most_common
1. 取出最常出現的元素
2. 根據其頻率排序(可指定要出現多少)
```python
# most_common method
words = ['a', 'b', 'a', 'c', 'd', 'f', 'a']
for word, count in Counter(words).most_common(10):
    print(word, count)
```