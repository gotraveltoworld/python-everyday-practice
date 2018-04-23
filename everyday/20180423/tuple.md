# Python tuple

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
2. 具有聚集(gather)和分散(scatter)的運算子，可以實現靈活的變數指派。
