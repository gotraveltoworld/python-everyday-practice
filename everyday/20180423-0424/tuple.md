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
            <class 'tuple'>
            ```
        - 不是`tuple`
            ```python
            t = ('a')
            type(t)
            <class 'str'>
            ```
        - 用關鍵字`tuple`建立
            ```python
            t = tuple()
            type(t)
            <class 'tuple'>
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