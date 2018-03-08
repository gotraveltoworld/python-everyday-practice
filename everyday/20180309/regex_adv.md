# Python string example.

* Basic regex function: https://repl.it/@Traveler/Python-String-practice-All
* Reference: http://zwindr.blogspot.tw/2016/01/python-regular-expression.html

> Pracetice python regex function.

* Add sub, subn function for replace function.
    - re = regular expression(regex)
    - sub = substitute(replace)

## regex.py
```python
def regex_functions(pattern='^Hello\W*world\!'):
    """
    flags:
        re.A, re.ASCII
        re.I, re.IGNORECASE
        re.L, re.LOCALE
        re.M, re.MULTILINE
        re.S, re.DOTALL
        re.U, re.UNICODE
        re.X, re.VERBOSE
        re.DEBUG
    """
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

    # 6. re.split(pattern, string, maxsplit=0, flags=0)
    match = re.split('\W', text)
    print('6.', match)

    # 7. re.findall(pattern, string, flags=0)
    match = re.findall(pattern, text)
    print('7.', match)

    # 8. re.finditer(pattern, string, flags=0)
    match = re.finditer(pattern, text)
    print('8.', match)

    # 9. re.sub(pattern, repl, string, count=0, flags=0)
    # https://docs.python.org/3/library/re.html#re.sub
    """
    Explanation:
    * re = regular expression(regex)
    * sub = substitute(replace)
    re.sub: 以regular pattern來偵測特定字串，並實行取代。應用於複雜的字串可以用pattern來取代符合的目標。
    """
    result = re.sub(pattern, text, 'Hi guys!', count=1)
    print('9.', result)

    # 10. re.subn(pattern, repl, string, count=0, flags=0)
    """
    Explanation:
    Official description: Perform the same operation as sub(), but return a tuple (new_string, number_of_subs_made).
    """
    result = re.subn(pattern, text, 'Hi guys!', count=1)
    print('10.', result)

```