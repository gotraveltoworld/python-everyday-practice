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

