# Python Text research.

### Link: https://repl.it/@Traveler/Simpletextresearch

## Topic:
1. Practice python's string method.
2. To solve some of word puzzles by python.

* text data resource:
    * http://wikipedia.org/wiki/Moby_Project
    * http://thinkpython2.com/code/words.txt
### word puzzles(字謎)
- palindromes(迴文)
- alphabetical order(字母順序)

palindromes(迴文)
```python
# palindrome <= 迴文
# noon, redivide
def is_palindrome(word):
    return word[::-1] == word

print(is_palindrome('noon')) # <= true

# Simple open text file and to read file content.
fin = open('words.txt')
print(fin.readline())
```

### main.py
```python
from first_print import print_text_from_file, get_file_content

def loop_print(file, strip_tex = False, limit = 10):
    line = 0
    for line_char in file:
        text = line_char.strip() if strip_tex == True else line_char
        print(line, '{0!r}'.format(text))
        line += 1
        # Limit the max line
        if (line > limit):
            break
if __name__ == '__main__':
    print_text_from_file()

    # Print \r\n
    loop_print(get_file_content())
    # Strip the text
    loop_print(get_file_content(), True)
```
### first_print.py
```python
# Simple open text file and to read file content.
def print_text_from_file():
    fin = open('words.txt')
    print(fin.readline())

def get_file_content(file_name = 'words.txt'):
    return  open('words.txt')
```
