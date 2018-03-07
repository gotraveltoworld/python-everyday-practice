# Python string example.
Basic regex function: https://repl.it/@Traveler/Python-String-practice-All

> Pracetice python regex function.

## regex.py
```python

# Use match method directly(example http format).
def http_filter(url):
    return re.match('^http[s]?:\/\/.*', url)

```