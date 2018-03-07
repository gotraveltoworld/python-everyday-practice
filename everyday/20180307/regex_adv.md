# Python string example.

Basic regex function: https://repl.it/@Traveler/Python-String-practice-All
Reference: http://zwindr.blogspot.tw/2016/01/python-regular-expression.html

> Pracetice python regex function.

## regex.py
```python
def regex_functions(pattern='^Hello\W*world\!'):
    text = r'Hello world!'

    # 1. re.compile(pattern, flags=0)
    compile_pattern = re.compile(text, re.IGNORECASE | re.VERBOSE)
    print('1.', compile_pattern)

    # 2. re.escape(string)
    escape = re.escape(text)
    print('2.', escape)  # Hello\ world\!

    # 3. re.search(pattern, string, flags=0)
    match = re.search(pattern, text)
    print('3.', match)

    # 4. re.match(pattern, string, flags=0)
    match = re.match(pattern, text)
    print('4.', match)

    # 5. re.fullmatch(pattern, string, flags=0)
    match = re.fullmatch(pattern, text)
    print('5.', match)
```