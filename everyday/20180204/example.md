# 用條件判斷式讓程式更簡潔
```python
# conditional expression
# Example 1-1
# Check the args default parameters.

def check_before(x):
    if x:
        return x
    else:
        return False

def check_after(x):
    return x if x else False

# Print result.
input = 100
print('check_before', check_before(input))
print('check_after', check_after(input))

```

# 用串列概括式讓List處理的更簡潔

```python
# Reference "https://openhome.cc/Gossip/Python/ForComprehension.html"
#  Example 2-1
scores = [('John', 95), ('Mark', 93), ('Marry', 99)]
print({name : score for (name, score) in scores})

#  Example 2-2, Create one list of two string combinations.
print([letter1 + letter2 for letter1 in 'John' for letter2 in 'Jack'])

# Examnple 2-3, Two dimensions list convert to one dimension list.
matrix = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]
print([element for row in matrix for element in row])

# Other example.
# According to the specified key to filter all duplicate elements.
db_iter = [ {'id': 1}, {'id': 1}, {'id': 2} ]
print({row.get('id'): row for row in db_iter if row.get('id', None)})
```
