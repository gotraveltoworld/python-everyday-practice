# Python's unicode methods.
* Basic practice: https://repl.it/@Traveler/Python-String-practice-All

* unicodedata:
    1. unicode
    2. string and unicode
    3. Test to print 'café'
    4. len to calculate unicode char's

## unicode_test.py
```python
# Show unicodedata
import unicodedata

def print_unicode(value='\u00a2'):
    name = unicodedata.name(value)
    result = unicodedata.lookup(name)
    print('{0}____{1}'.format(name, result))
    # CENT SIGN____¢

    # print café
    result = 'caf\u00e9'
    print(result)
    print(len(result))
```
