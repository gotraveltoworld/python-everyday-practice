# Python Text research.

### Link: https://repl.it/@Traveler/Simpletextresearch

## Topic:
1. Practice python's string method.
2. To solve some of word puzzles by python.
    - 9-1, 印出words長度20以上的單字
    - 9-2, 印出沒有字母e且長度20以上的單字
    - 9-2-1, 計算百分比(印出)
    - 9-3, 撰寫一個function(avoids)，兩個參數，分別是使用者輸入的字串，以及禁止的字母構成的字串，當輸入的字串沒有禁止的字母時回傳True。
        * 禁止的字母(string of forbidden letters)
        * 考慮使用者輸入的問題
    - 9-4, 寫出一個function(uses_only)，兩個參數，分別是使用者輸入的字串，以及允許的字母構成的字串，當輸入的字串只包含給定的允許字母清單中回傳True。
    - 9-5, 寫出一個function(uses_all)，兩個參數，分別是使用者輸入的字串，以及允許的字母構成的字串，當輸入的字串有用到給定允許字母清單中一次就回傳True。
        * Reduce to a previously solved problem (Combine the uses_only and uses_all)

* text data resource:
    * http://wikipedia.org/wiki/Moby_Project
    * http://thinkpython2.com/code/words.txt

```python
import sys
sys.path.append(sys.path[0])
fin = open('{0}\words.txt'.format(sys.path[0]))

# 9-3 avoids
def avoids(word, forbiddens=''):
    for w in word:
        if w in forbiddens:
            return False
    return True
# 9-4 uses_only
def uses_only(word, available=''):
    for w in word:
        if w not in available:
            return False
    return True
# 9-5 uses_all
def uses_all(word, required=''):
    for w in required:
        if w not in word:
            return False
    return True

# 9-5 uses_all by uses_only
def uses_all_v2(word, required=''):
    return uses_only(required, word)

print('Please, input your string of forbidden letters')
# forbiddens = input('input: ')
forbiddens = 'aeiou'
available = 'aeiou'
required = 'aeiou'

total = 0
allows = 0
uses = 0
needs = 0
needs_v2 = 0
for f in fin:
    total += 1
    word = f.strip()
    if avoids(word, forbiddens):
        allows += 1 # No forbidden letters.

    if uses_only(word, available):
        uses += 1 # Uses only.

    if uses_all(word, required):
        needs += 1

    if uses_all_v2(word, required):
        needs_v2 += 1

print(allows, uses, needs, needs_v2)
```