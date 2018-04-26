# Python data structures

### Practice on repl.it(https://repl.it/@Traveler)
1. [list repl.it](https://repl.it/@Traveler/listsfunctions)
2. [dict repl.it](https://repl.it/@Traveler/dictfunctions)
3. [tuple repl.it](https://repl.it/@Traveler/tuplefunctions)

### Study points
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
    - tuple
        1. common methods: `None`
        2. consists of items(keys: int or tuple=compound key, elements)
        2. Can use on each data structure with key and value.