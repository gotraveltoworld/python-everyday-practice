# Python data structures part II(exercises).

### Practice on repl.it(https://repl.it/@Traveler)
1. [data structures exercise](https://repl.it/@Traveler/DatastructurespartII)

Basic strcuture:
1. [list repl.it](https://repl.it/@Traveler/listsfunctions)
2. [dict repl.it](https://repl.it/@Traveler/dictfunctions)
3. [tuple repl.it](https://repl.it/@Traveler/tuplefunctions)
## 前言
本文根據習題來選用各種不同的資料結構。

### 基本資料結構(python)
1. 串列(list)
2. 字典(dict)
3. 元組(tuple)
4. 集合(set)

### 題目1
原文：
> As usual, you should at least attempt the exercises before you read my solutions.
__Exercise 13.1.__ Write a program that reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
Hint: The string module provides a string named whitespace, which contains space, tab, newline,
etc., and punctuation which contains the punctuation characters.
> Let’s see if we can make Python swear:
>   `>>> import string`
>   `>>> string.punctuation`
>   ```>>> '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'```
> Also, you might consider using the string methods strip, replace and translate
---

1. 13-1: 寫一隻程式讀取檔案，每行拆成單字。除去空白(whitespace)，與標點符號(punctuation)，並轉成小寫。
    * `from string import punctual` <= 讀取標點符號
    * 可參考`replace, strip, lower, translate`

```python
#!/usr/bin/python3
from string import punctuation
# Simply version.
def practice_one_simple():
    words = []
    with open('practice_1.txt') as fin:
        for f in fin:
            words += f.split(' ')

    clear_words = []
    for w in words:
        tmp_word = []
        for char in w.strip():
            if char in punctuation:
                pass
            else:
                tmp_word.append(char)
        clear_words.append(''.join(tmp_word).lower())
    return clear_words
```
### 題目2
原文：

> __Exercise 13.2.__ Go to Project Gutenberg (http: // gutenberg.org) and download your favorite
out-of-copyright book in plain text format.
Modify your program from the previous exercise to read the book you downloaded, skip over the
header information at the beginning of the file, and process the rest of the words as before.
Then modify the program to count the total number of words in the book, and the number of times
each word is used.
> Print the number of different words used in the book. Compare different books by different authors,
written in different eras. Which author uses the most extensive vocabulary?
>
> __Exercise 13.3.__ Modify the program from the previous exercise to print the 20 most frequently used
words in the book.
>
> __Exercise 13.4.__ Modify the previous program to read a word list (see Section 9.1) and then print all
the words in the book that are not in the word list. How many of them are typos? How many of
them are common words that should be in the word list, and how many of them are really obscure?
>