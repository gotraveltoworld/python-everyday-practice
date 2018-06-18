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
with open(file_name, 'r', encoding='utf-8') as content:
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

### 檔案操作相關(operate the file)

```python
# Use the write mode to open the file.

"""
file object = open(file_name [, access_mode][, buffering])
1. file_name：file_name is string depend on your file system.
2. access_mode：access_mode is a model about opening file, default is only read.

"""
# Model is write.
file_obj = open('words_open', 'w')
file_obj.write('First')
# 5 (回傳寫入的字元數量)
file_obj.write('Second')
# 6 (回傳寫入的字元數量)
file_obj.close()
# 關閉檔案操作
# file's content = FirstSecond
```

#### file object:
1. file.closed	return Boolean (True or False)
2. file.mode	get the model
3. file.name	get file name
#### About file Model
* Reference : http://www.runoob.com/python/python-files-io.html

Model  | Function  |
-------|:-------- |
r      | Default, only read|
rb     | Use binary format to open a file.|
r+     | Open file for writing and reading, point is putting at start.|
rb+    | (writing and reading)Use binary format to open a file, most of time to open an image or a document.|
w      | Open a file for writing. If the file exists, delete original content.|
wb     | Use binary format to open a file and to open a file for writing. If the file exists, delete original content.|
w+     | Open a file for writing and reading. If the file exists, delete original content.|
wb+    | (writing and reading)Use binary format to open a file. If the file exists, delete original content.|
a      | Open a file for adding new content.|
ab     | Use binary format to open a file. If the file exists, add new content after original content.|
a+     | Open a file for writing and reading. If the file exists, add new content after original content.|
ab+    | (writing and reading)Use binary format to open a file. If the file exists, add new content after original content.|

#### format operator
* Basic format method but you can use `string.format()` to replace the `%` operator.
```python
# % is a modulus operator.
# %d = digital.
# %g = float
# %s = string
int_42 = 42
print('%d' % int_42)
# 42
```

#### use os module to handle file
1. Absolute path: `/home/user/your_project/file_exe.py`
2. Relative path: `file_exe.py`
```python
import os
print(os.getcwd())
# /Absolute path.
print(os.path.abspath('files_data.md'))
# Show the file path.
print(os.path.exists('files_data.md')) #(True or False)
# Checking the file does exist or not.
print(os.path.isfile('files_data.md')) #(True or False)
# Checking the file is file or not.
```

#### File walk
用遞迴的概念寫檔案的遊走。
1. 遞迴呼叫自己本身
2. 利用`isfile`判斷是否要繼續往下層目錄移動
```python
import os
files = []
# listdir 列出目錄下的資料，回傳一個串列
def walk(dir_path=''):
    for name in os.listdir(dir_path):
        path = os.path.join(dir_path, name)

        if os.path.exists(path) and os.path.isfile(path):
            files.append(path)
        else:
            walk(path)
```

#### File walk
用遞迴的概念寫檔案的遊走。
1. 遞迴呼叫自己本身
2. 利用`isfile`判斷是否要繼續往下層目錄移動
```python
import os
files = []
# listdir 列出目錄下的資料，回傳一個串列
def walk(dir_path=''):
    for name in os.listdir(dir_path):
        path = os.path.join(dir_path, name)

        if os.path.exists(path) and os.path.isfile(path):
            files.append(path)
        else:
            walk(path)
```

#### Catch the exception
用例外捕捉的方式抓到一些執行例外
語法：`try...except`

範例：
```python
file_name = 'words_ex1~' # <= Error file name
try:
    content = open(file_name, 'r', encoding='utf-8')
    for line in content:
        print(line)

except IOError as io_err:
    print(io_err) # Output the exception message
    # [Errno 2] No such file or directory: 'words_ex1~'

# You can use 'with' statement
with open(file_name, 'r', encoding='utf-8') as content:
    for line in content:
        print(line)
# [Errno 2] No such file or directory: 'words_ex1~'
```
`with`是一種content(上下文)管理器，[Reference](https://eastlakeside.gitbooks.io/interpy-zh/content/context_managers/)

#### Database
寫入資料庫的套件(Only use on Unix)

```python
# https://docs.python.org/3/library/dbm.html
import dbm
db = dbm.open('dbm', 'c')
db['one'] = 1
print(db['one'])
```
##### Model:
Value  | Meaning  |
-------|:-------- |
r      | Open existing database for reading only (default)|
w      | Open existing database for reading and writing.|
c      | Open database for reading and writing, creating it if it doesn’t exist.|
n      | Always create a new, empty database, open for reading and writing.|

特點:
1. 可以用字典(dict)形式存取
2. 讀取的檔案以位元組(bytes object)呈現
3. 可以用`for ... in ...`形式存取


### Pickling
dbm限制鍵和值都必須是字串或是位元組，如果用其他資料結構會出現錯誤。所以可以用`pickling`轉換成適合的字串。

```python
import pickle

t = [1, 2, 3]
s = pickle.dumps(t)
# b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
pickle.loads(s)
# [1, 2, 3]
```

`pickling`和`un-pickling`有物件拷貝的效果(`shelve`)。

### PIPE(shell: command-line interface)

```python
import os

cmd = 'ls -la'
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(stat)
```
UNIX可以用`md5sum`的方式來驗證兩個檔案之間是否相同，其相同的概率非常小。

```python
import os

filename = 'book'
cmd = 'md5sum {0}'.format(filename)
fp = os.popen(cmd)
res = fp.read()
print(res)
# f0adb01ecd7c1cbb66884de181e08c53  book
stat = fp.close()
print(stat)
# None
```
