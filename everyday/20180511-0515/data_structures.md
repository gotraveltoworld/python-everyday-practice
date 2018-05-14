# Python data structures part II.

### Practice on repl.it(https://repl.it/@Traveler)
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

### 題目
1. 13-1: 寫一隻程式讀取檔案，每行拆成單字。除去空白(whitespace)，與標點符號(punctuation)，並轉成小寫。
    * `from string import punctual` <= 讀取標點符號
    * 可參考`replace, strip, lower, translate`
```python
#!/usr/bin/python3
from string import punctuation

def practice_one():
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
