# Python string basic method
### Practice
1. strip, replace, find
2. count
3. use a slice to exact string(palindrome).


練習範例： https://repl.it/@Traveler/Python-String-practice-3

```python
# Reference: 'https://openhome.cc/Gossip/Python/StringType.html'
text = ' banana '
print(text.strip())
print(text.replace('na', '_na_'))
print(text.find('b'))
print(text[-3:-1])
# Common reversed string
print(text[::-1]) # <= Show reversed
print(text.count('a')) # 3

# palindrome <= 迴文
# noon, redivider
def is_palindrome(word):
    return word[::-1] == word

print(is_palindrome('bye'))
print(is_palindrome('noon'))
```