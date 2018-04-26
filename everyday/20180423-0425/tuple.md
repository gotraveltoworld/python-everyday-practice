# Python tuple
### Link: https://repl.it/@Traveler/tuplefunctions

## Content:
1. tuple(元組)是不可變(immutable)的資料結構
    * index是正整數和list相同
    * 語法上用',' (comma) 區隔每個元素
    * 常用的寫法是將元組寫在括號中('parentheses')
        - 舉例: ` t = ('a', 'b', 'c')`
        - 建立單一元素:
            ```python
            t = 'a',
            type(t)
            # <class 'tuple'>
            ```
        - 不是`tuple`
            ```python
            t = ('a')
            type(t)
            # <class 'str'>
            ```
        - 用關鍵字`tuple`建立
            ```python
            t = tuple()
            type(t)
            # <class 'tuple'>
            ```
        - 引數是字串的時候
            ```python
            t = tuple('abc')
            print(t)
            ('a', 'b', 'c')
            ```
        - 關係運算子，從左自右比較，當其中一元素符合就不會考慮後續的元素，如下範例，當比較到第二個的元素就符合條件，因此後續的比較不會進行。
            ```python
            (0, 1, 2) < (0, 3, 4)
            # True
            (0, 1, 2000000) < (0, 3, 4)
            # True
            ```
2. 元組指派與交換(swap)
    - `a, b = b, a` ((swap, tuple assignment))
    - `a, b, c = 1, 2, 3`
    - `a, b = '95'`
3. 元組可作為多值回傳
    - Multiple returns.
        ```python
        # One-method
        t = divmod(7, 3)
        print(t)
        # (2, 1)

        # Two-method
        quot, rem = divmod(7, 3)
        print(quot, rem)
        # (2, 1)
        ```
3. 具有聚集(gather)和分散(scatter)的運算子，可以實現靈活的變數指派。
    - gather & scatter:
        ```python
        # gather.
        def printall(*args):
            print(args)
        printall(1, 2,.0, '3')
        print(printall)

        # scatter
        t = (7, 3)
        t = divmod(*t) # <= scatter.
        # (2, 1)
        ```
    - sum practice:
        ```python
        t = (7, 3, 10)
        def sumall(*args):
            return sum(args)

        print(sumall(*t))
        # 20
        ```
4. `zip`函式可以傳入兩個以上的串列或是元組，回傳一個由元組作為元素的串列，舉例：`[(1, 2), (3, 4)]`。其中每個元素是個來自不同串列或元組的元素。此函式的名稱由來是`zipper(拉鍊)`。
    - zip: 結果會是一個`zip object`
        ```python
        s = 'abc'
        a = [0, 1, 2]
        zip(s, a)
        # [('a', 0), ('b', 1), ('c', 2)],
        print(zip(s, a))
        # <zip object at 0x7f4d4da1cb48>
        for i in zip(s, a):
            print(i)
            # ('a', 0)
            # ('b', 1)
            # ('c', 2)
        ```
    - 簡潔創建字典的方法:
        ```python
        d = dict(zip('abc', range(3)))
        print(d)
        # {'a': 0, 'c': 2, 'b': 1}
        ```
    - 元組的不可變性(immutable)可以作為鍵值，舉例：假設電話號碼需要姓名和地址作為複合主鍵，就像這樣`dic[name, address] = tel_number`。
