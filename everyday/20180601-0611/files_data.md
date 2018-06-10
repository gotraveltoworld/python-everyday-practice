# Python file data.

### Practice on repl.it(https://repl.it/@Traveler)
1. [file functions](https://repl.it/@Traveler/Openfilefunctions)

## 前言
本文練習操作檔案以及一些背景執行的指令。

### Exercise 'startswith' http://www.runoob.com/python/att-string-startswith.html
```python
# startswith, 檢查字串開頭是否符合，符合回傳True, 否則回傳False
start_with = 'aardwolf'
file_name = 'words_ex1'
with  open(file_name, 'r', encoding='utf-8') as content:
    for line in content:
        if line.startswith(start_with):
            print(line)
# result: aardwolf

# words_ex1
'''
aa
aah
aahed
aahing
aahs
aal
aalii
aaliis
aals
aardvark
aardvarks
aardwolf <= Start with.
aardwolves
'''
```

