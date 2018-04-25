# Python dict practice.
### Link: https://repl.it/@Traveler/dictfunctions

## Practices
1. 11-1: 讀取words.txt，儲存所有文字作為鍵值，並用`in`運算子檢查是否在字典中。
    ```python
    import sys
    sys.path.append(sys.path[0])
    fin = open('{0}/words.txt'.format(sys.path[0]))

    for f in fin:
        key = '{0}'.format(f.strip())
        dic[key] = ''
    if 'aa' in dic:
        print('aa') # aa
    else:
        print('No')
    ```
2. 11-2 用`setdefault`改寫‵`invert_dict`方法
    ```python
    def invert_dict_adv(dic = {}):
        """Inverts a dictionary, returning a map from val to a list of keys.
        反轉字典，並回傳一個由val映射到鍵值的列表
        """
        inverse = {}
        for key in dic:
            val = dic[key]
            # Convert new list.
            inverse.setdefault(val, []).append(key)
        return inverse
    ```
3. 11-3 `memo (memoize)`化，練習阿克曼函數(Ackermann function)，試著使用memo化的版本是否能估算較大引數。由於遞迴函式增長得非常快，因此可以考慮用外部紀錄變數。
    * [阿克曼函數維基百科](https://zh.wikipedia.org/wiki/%E9%98%BF%E5%85%8B%E6%9B%BC%E5%87%BD%E6%95%B8)
    * [阿克曼函數資料結構](http://notepad.yehyeh.net/Content/DS/CH02/7.php)

    ```python
    # Reference from http://greenteapress.com/thinkpython2/code/ackermann_memo.py
    cache = {}
    def ackermann(m, n):
        """Computer the Ackermann function A(m, n)

        n, m: non-negative integers.
        """
        if m == 0:
            return n + 1
        if n == 0:
            return ackermann(m - 1, 1)

        if (m, n) in cache:
            return cache[m, n]
        else:
            cache[m, n] = ackermann(m - 1, ackermann(m, n - 1))
            return cache[m, n]

    print(ackermann(3, 4))
    print(ackermann(3, 6))
    ```
4. 改寫`has_duplicates`，符合dict版本
    ```python
    # Use the list comprehension and Counter module.
    from collections import Counter
    def has_duplicates(array):
        return  any(int(r) > 1 for r in [v for v in Counter(array).values()])

    # Use the dict and for-loop.
    def has_duplicates2(array):
        dic = {}
        for x in array:
            if x in dic:
                return True
            dic[x] = True
        return False

    # Use the Set(Compare origin and set data)
    def has_duplicates3(array):
        return len(set(array)) < len(array)
    ```
5. 11-5 運用rotate(caesar_cypher.py)轉動文字來得到另一個字，如果字彙表中有符合的文字就可稱為轉動對組(rotate pairs)。
    ## Import caesar_cypher.py and to rotate.
    ```python
    # Caesar cipher, https://zh.wikipedia.org/wiki/%E5%87%B1%E6%92%92%E5%AF%86%E7%A2%BC
    """
    1. ord: text to number.
    2. chr: number to text.
    """
    def rotate_letter(letter, shift=2):
        # Check lower or upper.
        if letter.isupper():
            start = ord('A')
        elif letter.islower():
            start = ord('a')
        else:
            return letter

        # Reset the start point.
        char = ord(letter) - start
        # To shift base on (letter's:26).
        cypher = ((char + shift) % 26) + start
        return chr(cypher)

    def cypher(plain_text, shift=2):
        cypher_text = ''
        for c in plain_text:
            cypher_text += rotate_letter(c, shift)

        return cypher_text

    def rotate_pairs(words):
        count = 1
        for w in words:
            if (cypher(w, 1) in words):
                print(w, cypher(w, 1))
                # Show all rotate pairs.
                count += 1
        return count
    # print 61 rotate pairs
    ```
6. 11-6 Car-talk puzzlers [__原文:(Wordplay Anyone?)__](https://www.cartalk.com/content/wordplay-anyone)。本謎題主要是根據英文的音節(`syllable`)來判斷其差異性，所以會借用外部的語音辭典的資料，[__語音字典下載__](http://greenteapress.com/thinkpython2/code/c06d)
    * 運用字典的性質，比對出是否有存在相同的元素
    * 運用讀檔的方法，讀取語音辭典及文字列表
    * 運用列表切片的方式(slice)，簡潔處理所有文字的組合
