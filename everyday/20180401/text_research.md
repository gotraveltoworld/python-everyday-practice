# Python Text research.

### Link: https://repl.it/@Traveler/Simpletextresearch

## Topic:
1. Practice python's string method.
2. To solve some of word puzzles by python.
    - 9-1, 印出words長度20以上的單字
    - 9-2, 印出沒有字母e且長度20以上的單字

* text data resource:
    * http://wikipedia.org/wiki/Moby_Project
    * http://thinkpython2.com/code/words.txt

```python
import sys
sys.path.append(sys.path[0])
fin = open('{0}\words.txt'.format(sys.path[0]))

# 印出超出特定字元的單字
def get_specify_len(word='', length=20):
    if len(word) > length:
        return '{0!r}'.format(word)
    else:
        return ''

# 當英文單字中沒有包含特定字母時回True
def has_no(word='', alphabet='e'):
    if alphabet not in word:
        return True

for f in fin:
    word = get_specify_len(f, length=20)
    if word and has_no(word):
        print(word)
        # 'microminiaturization\n'
        # 'microminiaturizations\n'
```