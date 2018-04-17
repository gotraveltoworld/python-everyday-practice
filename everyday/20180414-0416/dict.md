# Python lists function.
## Link: https://repl.it/@Traveler/dictfunctions
## Content:
1. 字典(dictionary)是一種映射形式的資料結構，
    * dict的index幾乎可以是任何形式的型別，不同於list，必須要是正整數。
    * 一個dict含有索引構成的群集(a collections of indices)，就是keys和values。這種key和value構成的關聯稱為鍵值與值對組(key-value pair)，有時也可以稱為項目(item)。
    * `ditc`這個方法可以建立一個空的dict。
    * 顯示的符號是`{}`(squiggly brackets)，代表空的字典(empty dictionary)。指定特定的鍵與值可以用`[]`(square brackets)指派，例如：`dic['key']  = 'Hi'`。
    * dict是無序的元素組合，運用雜湊表(hashtables)的方式來降低查找元素的時間。
    * dict可用len計算__鍵值__的數量。
    * dict用`in`運算子，可以找出在__鍵值__中有存在的索引。如果要找值，需要使用`dict.values()`進行比對。
2. 字典(dict)可以做為計數器的一個群集。
    * 利用鍵與值對應，可以計算每個每個鍵值出現的次數，例如：計算文本中所有英文字母出現的次數，就可以用26字母當作鍵值，值則是次數，就可以很好的表示各個字母出現的次數。
    * 利用鍵值的唯一性，可以根據需要創建資料結構
    ```python
    # histogram application.
    def histogram(text = ''):
        dic = dict()
        for c in text:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        return dic

    string1 = 'abcdefghijklmnopqrstuvwxyz'
    string2 = string1.upper()
    print(histogram(string2))
    ```
3. 用`for`巡訪字典鍵值(再用鍵值取出資料)，例如:
    ```python
    def print_hist(h):
        for c in h:
            print(c, h[c])
    ```
4. 查找(lookup)，就是用key查找資料的一種方式，例如：`v = d[k]`。反向就是用值去查找`value`，稱為 __反向查找__ `reverse lookup`，但是因為反向的關係，必須用`search`的方式處理。
    ```python
    # Search pattern: 搜尋模式, (raise statement, is a exception statement)
    def reverse_lookup(d, v):
        for k in d:
            if d[k] == v:
                return k
        raise LookupError() # Lookup's Error.
    ```
    反向查找比正向查找慢很多，所以如果需要頻繁用到的話應該考慮改採其他資料結構。
    ```python
    # 補充訊息：可回傳錯誤訊息
    raise LookupError('value does not appear in the dictionary.')
    ```
5. 字典(dict)和串列(list)的比較：
    * 參照上述幾點，當賦予一個新的字典，它可以將字母產生鍵值，並且對應的出現的頻率(字頻)上。如果想要反轉(inverts)結果，也可以用一個函式來實作。
    ```python
    def invert_dict(dic):
        inverse = {}
        for key in dic:
            val = dic[key]
            if val not in inverse:
                inverse[val] = [key]
            else:
                inverse[val].append(key)
        return inverse

    hist = histogram('abcabcdpap')
    print(hist)
    print(invert_dict(hist))
    # {'a': 3, 'b': 2, 'c': 2, 'd': 1, 'p': 2}
    # {3: ['a'], 2: ['b', 'c', 'p'], 1: ['d']}
    ```
    * 串列和字典都是可被改變的資料型態，因此不可作為 __鍵值__ ，因為必須要是 __可雜湊(hashable)__ ，但是可以作為值存在。
