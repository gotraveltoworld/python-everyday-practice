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
> Let’s see if we can make Python swear:<br>
>   `>>> import string`<br>
>   `>>> string.punctuation`<br>
>   ```>>> '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'```<br>
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
#### exercise_examples
```python
# 13.3
# filter all punctual and to lower
#!/usr/bin/python3
from collections import Counter
from string import punctuation

def load_words(path='exercise_1.txt'):
    # Load file
    words = []
    with open(path) as fin:
        for f in fin:
            words += f.split(' ')
    return words

def filter_punctual(words):
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

def exercise_one_simple():
    words = load_words()
    return filter_punctual(words)
# Output most_common words.
def exercise_two(common=20):
    words = load_words('book1.txt')
    new_words = [w for w in filter_punctual(words) if w]
    return Counter(new_words).most_common(common)

def exercise_single_word(file='book1.txt'):
    words = load_words(file)
    return [
        w for w in filter_punctual(words) if w
    ]
```
#### main.py
```python
if __name__ == '__main__':
    book1 = set(exercise_single_word('book1.txt'))
    book2 = set(exercise_single_word('book2.txt'))
    print(len(book1 - book2)) # 854
    # for exercise 13.4
    words_list = set(exercise_single_word('words.txt'))
    print(len(book1 - words_list)) # 555
```

#### 重點
1. `from string import punctuation`可以用來判斷標點符號。
2. string是不可變的資料結構，每次的變動都是完全不同的一個變數。
3. string處理可以常用的有`replace`, `translate`等等方法。
4. string是可以進行迭代(iterable)的物件。
5. word frequently很常用於文字分析。

### 題目3
原文： [link](http://greenteapress.com/thinkpython2/html/thinkpython2014.html)
> __Exercise 5__
> Write a function named choose_from_hist that takes a histogram as defined in Section 11.2 and returns a random value from the histogram, chosen with probability in proportion to frequency. For example, for this histogram:
>
> `>>> t = ['a', 'a', 'b']`<br>
> `>>> hist = histogram(t)`<br>
> `>>> hist`<br>
> `{'a': 2, 'b': 1}`<br>
> your function should return 'a' with probability 2/3 and 'b' with probability 1/3.

#### choose_from_hist.py
```python
import random
# Calculate the histogram.
def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
# Calculate the percentage.
def choose_from_hist_percentage(list_words):
    total = sum([word for index, word in list_words.items()])
    return {
        index:'{0:.2%}'.format(float(word/total))
            for index, word in list_words.items()
    }
# Handle all probability
def choose_from_hist(hists):
    total = sum([word for index, word in hists.items()])
    x = random.randint(0, total)
    val = 0
    for k, w in hists.items():
        if k == 0:
            val = w
        else:
            val += w

        if x < val:
            return k
```

### author's example
```python
import string
# process_file loops through the lines of the file, passing them one at a time to process_line. The histogram hist is being used as an accumulator.
def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist
# process_line uses the string method replace to replace hyphens with spaces before using split to break the line into a list of strings.
def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

# most_common, The function will return a list of word-frequency tuples.
def most_common(hist={}):
    return sorted([(w, k) for w, k in hist.items()], key=lambda s: s[1], reverse=True)
# Other sort methods: https://wiki.python.org/moin/HowTo/Sorting.
```
#### 重點
1. `strip`可以用來直接移除標點符號和空白(`punctuation`and`whitespace`)
2. string是不可變的資料結構，所以只能回傳新的string。

#### 選擇性參數
原文：
> We have seen built-in functions and methods that take optional arguments. It is possible to write programmer-defined functions with optional arguments, too. For example, here is a function that prints the most common words in a histogram
>
For example:
```python
# num gets the value of the argument instead.
# In other words, the optional argument overrides the default value.
def print_most_common(hist, num=10):
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]: # <= reverse t[:num].
        print(word, freq, sep='\t')
    """
    The most common words are:
        5295	to
        5266	the
        4931	and
        4339	of
        3191	i
        3155	a
        2546	it
        2483	her
        2400	was
        2364	she
    """
```