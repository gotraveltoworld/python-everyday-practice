# Python map function

### link: https://repl.it/@Traveler/Python-build-in-functions
### Reference: http://www.runoob.com/python/python-func-map.html
1. recursive function
2. return statement

## recursion.py
```python
# map(callback function, iterable, ...)

print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
# [1, 4, 9, 16, 25]

list_a = [1, 2, 3]
list_b = [5, 6, 7, 8]
list_c = [11, 12, 13, 14]
list_result = list(map(lambda x, y, z : x + y + z, list_a, list_b, list_c))
print(list_result)
# [17, 20, 23]  <= 以最少的元素列表為主
```