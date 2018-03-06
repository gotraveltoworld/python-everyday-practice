# Python string basic method
### String Method
1. Akind of Sequence
2. Ordered collection
3. Immutable

練習範例： https://repl.it/@Traveler/Python-String-practice

練習基本字串的定義和語法，進階部分後續會再持續練習。

```python
# Simple case.
fruit = 'banana'
print(fruit[0])
# b
# Reversed, to use the negative index.
print(fruit[-1])
# a

# Traversal all string by while loop.
index = 0
while index < len(fruit):
    print(fruit[index])
    index += 1

def reversed_print_text(text):
    index = 0
    while index > -len(text):
        print(text[index])
        index -= 1

reversed_print_text(text)

# Concatenation
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        letter += 'u'
    print(letter + suffix)

# String segment.
print(fruit[0:3])# from index 0 to (3-1)
print(fruit[:3]) # from index 0 to (3-1)
print(fruit[0:]) # from index 0 to end
print(fruit[:]) # All string


# String search(find function)
def find(words, letter, strat=0):
    for index, word in enumerate(words[strat:]):
        if word == letter:
            return index
    return -1

print(find('bye', 'b')) # 0
print(find('bye', 'b', 1)) # -1

# Count letter number.
def count(words, letter, strat=0):
    conuts = 0
    for word in words[strat:]:
        if word == letter:
            conuts += 1
    return conuts

print(count('bye', 'b')) # 0
print(count('bye', 'b', 1)) # -1
```