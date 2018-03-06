# Python string example.
All string(from basic to advantage)： https://repl.it/@Traveler/Python-String-practice-All

> Pracetice Caeasar cypher

1. Shift all string base on the same step size.
2. Include two parameters(origin plain text, shift step size). For example, A rotating three to become D.
* Use 'ord' function.

## caesar_cypher.py
```python
# Caesar cipher, https://zh.wikipedia.org/wiki/%E5%87%B1%E6%92%92%E5%AF%86%E7%A2%BC
"""
1. ord: text to number.
2. chr: numer to text.
"""
def rotate_letter(letter, shift=2):
    # Check lower or upper.
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    # Reset the start point.
    char = ord(letter) - start
    # To shift base on (letter's:26).
    cypher = ((char + shift) % 26) + start
    return chr(cypher)

def cypher(plain_text, shift=2):
    cypher_text = ''
    for c in plain_text:
        cypher_text += rotate_letter(c, shift)

    return cypher_text

```