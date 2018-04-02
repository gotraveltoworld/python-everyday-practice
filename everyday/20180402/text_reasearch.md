# Python Text research.

### Link: https://repl.it/@Traveler/Simpletextresearch

## Topic:
1. Practice python's string method.
2. To solve some of word puzzles by python.
    - 9-1, 印出words長度20以上的單字
    - 9-2, 印出沒有字母e且長度20以上的單字
    - 9-2-1, 計算百分比(印出)

* text data resource:
    * http://wikipedia.org/wiki/Moby_Project
    * http://thinkpython2.com/code/words.txt

```python
import sys
sys.path.append(sys.path[0])
fin = open('{0}\words.txt'.format(sys.path[0]))

# 當英文單字中沒有包含特定字母時回True
def has_no(word='', alphabet='e'):
    if alphabet not in word:
        return True
    else:
        return False

total = 0
e_number = 0
for f in fin:
    if has_no(f):
        e_number += 1# Has no 'e'
    else:
        pass # Skip
    total += 1

percentage = '{0!s:.6}%'.format((e_number/total) * 100)
print(percentage)
# 33.073%

# other solution(list comprehension).
fin = open('{0}\words.txt'.format(sys.path[0]))
e_number = len([f for f in fin if has_no(f)])
fin = open('{0}\words.txt'.format(sys.path[0]))
total = len([f for f in fin])
percentage = '{0!s:.6}%'.format((e_number / total)* 100)
print(percentage)
```