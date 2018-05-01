# Python data structures

### Practice on repl.it(https://repl.it/@Traveler)
1. [list repl.it](https://repl.it/@Traveler/listsfunctions)
2. [dict repl.it](https://repl.it/@Traveler/dictfunctions)
3. [tuple repl.it](https://repl.it/@Traveler/tuplefunctions)

### Study points(english)
* mutable(unhashable):
    - list
        1. common methods: `.append(), .pop(), .remove(), .reverse(), .sort(), del`
        2. consists of items(keys: common is int, values)
        3. `for item in list` <= `item == each element`.
        4. Can use on each data structure with value but not use on key.
    - dict
        1. common methods: `.get, , .keys(), .values(), .items(), .clear()`
        2. consists of items(keys: is string or int or tuple=compound key, elements)
        3. `for item in list` <= `item == each key`.
        4. Can use on each data structure with value but not use on key.
* immutable(hashable)
    - str
        1. common methods: `.format(), .split(), strip()`
        2. consists of items(keys: int, elements)
        3.  Can use on each data structure with key and value.
    - tuple
        1. common methods: `None`
        2. consists of items(keys: int or tuple=compound key, elements)
        3. Can use on each data structure with key and value.


### Study points(chinese)
* 可變的資料型別(不可雜湊:unhashable):
    - 串列(list)
        1. 常用方法: `.append(), .pop(), .remove(), .reverse(), .sort(), del`
        2. 組成項目(鍵值是整數, 值可以是任意資料型別)
        3. `for item in list` <= `item == each element`.
        4. 可以作為其他資料型別的值，但不能作為鍵值
    - 字典(dict)
        1. 常用方法: `.get, , .keys(), .values(), .items(), .clear()`
        2. 組成項目(鍵值可以是字串、整數或是元組, 值可以是任意資料型別)
        3. `for item in list` <= `item == each key`.
        4. 可以作為其他資料型別的值，但不能作為鍵值
* 不可變的資料型別(可雜湊:hashable)
    - 字串(str)
        1. 常用方法:`.format(), .split(), strip()`
        2. 組成項目(鍵值是整數, 值是字元)
        3. 可以作為其他資料型別的鍵值
    - 元組(tuple)
        1. 常用方法: `None`
        2. 組成項目(鍵值是整數, 值可以是任何資料型別)
        3. 可以作為其他資料型別的鍵值