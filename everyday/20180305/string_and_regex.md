# Python string example.
Basic regex function: https://repl.it/@Traveler/Python-String-practice-All

> Pracetice python regex function.

## regex.py
```python
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/library/re.html#module-contents
# http://zwindr.blogspot.tw/2016/01/python-regular-expression.html
import re

def simple_re(pattern=r'^test', text='test'):
    # Allow multile regular expression pattern, 're.VERBOSE'
    # https://docs.python.org/3/library/re.html#module-contents
    return re.compile(pattern, re.VERBOSE).match(text)

```

### Regular, module-contents

| Name | Descript |
| :------| ------: |
| re.ASCII | 比對ASCII|
| re.DEBUG | 顯示比對邏輯 |
| re.IGNORECASE | 忽略大小寫 |
| re.LOCALE | 根據本機端編碼比對 |
| re.MULTILINE | 比對每一行 |
| re.DOTALL | 比對所有文字，連換行也會比對 |
| re.VERBOSE | 允許在比對邏輯內撰寫註解 |