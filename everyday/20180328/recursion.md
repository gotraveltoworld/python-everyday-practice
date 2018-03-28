# 條件式

### link: https://repl.it/@Traveler/conditions-and-recursion

1. recursive function
2. return statement

## recursion.py
```python
def recursion(n):
    if n <= 0:
        print('n = 0')
    else:
        print(n)
        recursion(n - 1)
```