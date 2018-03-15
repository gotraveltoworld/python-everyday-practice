# Python string example.

* Basic function: https://repl.it/@Traveler/Python-String-practice-All
* Reference: https://www.tutorialspoint.com/python/string_endswith.htm
Study the format function.
* Some of string method
    - endswith(), 判斷是否是子字串, 提供開始後結束的索引。
        - 回傳True or False
    - istitle(), 檢查每個字的第一個字元是否都是大寫

## str_format.py
```python
def basic_method(text=' my name is Traveler. '):
    print(text.strip()) # My name is Traveler.
    print(text.strip().capitalize()) # My name is Traveler.
    print(text.strip().swapcase()) # MY NAME IS tRAVELER.
    suffix = "Traveler"
    print(text.endswith(suffix))
    print(text.endswith(suffix, 20))

    print(text.endswith(suffix, 11, 20))
    print(text.endswith(suffix, 5, 15))

def show_title(text=' My name is Traveler. '):
    print(text.istitle())

```