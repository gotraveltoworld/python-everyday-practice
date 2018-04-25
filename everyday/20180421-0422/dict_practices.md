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
3. 11-3 `memo (memoize)`化，練習阿克曼函數(Ackermann function)，試著使用memo化的版本是否能估算較大引數。由於遞迴函式增長得非常快，因此可以考慮用外部紀錄變數。
    * [阿克曼函數維基百科](https://zh.wikipedia.org/wiki/%E9%98%BF%E5%85%8B%E6%9B%BC%E5%87%BD%E6%95%B8)
    * [阿克曼函數資料結構](http://notepad.yehyeh.net/Content/DS/CH02/7.php)

    ```python
    # Reference from http://greenteapress.com/thinkpython2/code/ackermann_memo.py
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
