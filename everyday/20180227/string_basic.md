# Python string basic method
### String Method
1. Akind of Sequence
2. Ordered collection
3. Immutable

練習範例： https://repl.it/@Traveler/Python-String-practice-1

```python
# Immutable
text = 'banAna'
try:
    text[0] = 'a'
except Exception as e:
    print(e)
"""
Traceback (most recent call last):
  File "python", line 60, in <module>
TypeError: 'str' object does not support item assignment
"""

# String attribute.(upper, lower)
print(text.upper())
print(text.lower())

# find in string.
print('a' in text) # True
print('text' in text) # False

# Compare two string.
"""
1. Use relational operators to compare two string.
2. Test the '<', '>', '=' for alphabetical order.
    * 大寫在小寫之前
    * 如果要排序，記得要先轉換大小寫成相同格式
"""
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)
in_both('apples', 'oranges')
"""
a
e
s
"""
text = 'banana'
word = 'Pineapple'
if word < text:
    print('You word {0}, comes before {1}'.format(word, text))
elif word > text:
    print('You word {0}, comes after {1}'.format(word, text))
else:
    print('All reight, {0}'.format(text))

# Debug method.
def is_reverse(word1, word2):
    # Guardian pattern.
    if len(word1) != len(word2):
        return False

    i = 1
    for w1 in word1:
        if w1 != word2[-i]:
            return False
        i += 1
    return True

print(is_reverse('stops', 'potss')) # False
print(is_reverse('stop', 'pots')) # True
```