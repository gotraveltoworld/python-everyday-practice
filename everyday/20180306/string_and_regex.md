# Python string example.
Basic regex function: https://repl.it/@Traveler/Python-String-practice-All

> Pracetice python regex function.

## regex.py
```python

# Use match method directly(example http format).
def http_filter(url):
    return re.match('^http[s]?:\/\/.*', url)
```

## Basic Syntax
* '.' : 比對除了`\n`以外的字元
* '^' : 字串 __開頭__ 必須符合該字元
* '$' : 字串 __結尾__ 必須符合該字元
* '*' : 至少 __零次__ 的比對
* '+' : 至少 __一次__ 的比對
* '?' : 至少 __零或一次__ 的比對
* '*?', '+?', '??' : 符合最少的字元(non-greedy)，不需要全部符合，只要符合一個就可以算是比對完成。
* '\' : 跳脫字元，如果要比對`\`就必須改用`\\`這樣的形式。
* '[]' : 集合，常用於英文和數字
    - a-z, A-Z, 0-9 <= 常用比對模式
    - For example: [a-zA-Z0-9], 代表比對所有英文字母和阿拉伯數字。
* '|' : or(或者)
* '(...)' : 取得框框內的字串
* '(?:...)' : 不取得框框內的字串
* '(?=...)' : __之後__ 的字串要符合，不會放入group裡面
* '(?!...)' : __之後__ 的字串不能符合，不會放入group裡面
* '(?<=...)' : __之前__ 的字串不能符合，不會放入group裡面
* '(?<!...)' : __之前__ 的字串不能符合，不會放入group裡面
