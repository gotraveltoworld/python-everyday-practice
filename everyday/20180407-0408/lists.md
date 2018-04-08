# Python lists function.

### Link: https://repl.it/@Traveler/Simpletextresearch

## Content:
1. Write some list functions and features.
2. List some of function to describe the list features.
    * A kind of sequence.
    * Each values to call the 'elements' or 'items'.
    * Use '[]'(square brackets) to create the list, for example '[10, 20, 30]'
    * You can include other list into the list(nested)
    * List is mutable, you car assign a new value to replace existing value.
3. Use loop or indices to operate the value.
    * for loop(in): `for r in list`
        - range: to create a new iterator for your task. For example : `range(10)`
        - len: to get list length
    * indices: `list[0] = 1`, begin index of zero.
    * You can use any integer expression to get or set new value into list.
    * If the index doesn't exist, you will receive the IndexError exception.
    * You can use 'in' operator to operate the list content.
4. Operator
    * Concatenates: `[1, 2] + [3, 4]`, `[1, 2, 3, 4]`
    * Multiply: `[0] * 4`, `[0, 0, 0, 0]`
5. Slice operator(Some syntax)
    * `a = [1, 2, 3, 4, 5]`
    * `a[1:3]`
    * `[2, 3]`
6. Functions
    * append: `a = [1]`, `a.append(2)`, `[1, 2]`
    * extend: `a = [1], b = [2]`, `a.extend(b)`, `[1, 2]`
    * sort: `a = [2, 1]`, `a.sort()`, `[1, 2]`
7. Map, Filter, Reduce
    * Map: operate all elements by the callback function, to return new list.
    * Filter: filter all elements by a specified condition, to return existing list(by filter).
    * Reduce(約簡): get all elements to convert one value(ex: sum of values)
        - `sum([1, 2, 3])`, `6`
8. Remove, pop, del
    * pop(specify index to return value, if you don't set index, to return last element): `a = [1, 2 ,3]`, `a.pop(1)`, `[1, 3]`
    * del(if you only want to specify index to delete, you can use del): `a = [1, 2, 3]`, `del a[1]`, `[1, 3]`
        - If you wnat to delete multiple values, you can use the 'del + slice operator', `del a[0:3]`
    * remove(if only want to remove the value, but you don't know the index, you can use the remove function, to return `None`): `a = ['a', 'b', 'c']`, `a.remove('b')`, `['a', 'c']`
9. List and string
    * To convert string to list. `s = 'abc'`, `t = list(s)`, `['a', 'b', 'c']`
    * split: `s = 'string1 string2 string3'`, `t = s.split()`, `['string1', 'string2', 'string3']`, you can use the 'delimiter(區隔符)' to divide the string.
    * join: `t = ['s', 't', 'r', 'i', 'n', 'g']`, `','.join(t)`, `'s,t,r,i,n,g'`
10. Object and value(Call by reference and Call by value)
    * String: `a = 'ab'`, `b = 'ab'`, `a is b <= True`
    * List: `a = [1]`, `b = [1]`, `a is b <= False`
    * Equivalent(具有相同元素) and identical(參考相同物件): 等效和同一，代表list是參考同一物件還是具有相同元素。
11. 別名(alias name) and list's reference
    * `a = [1], b = a` b is a alias name, because the a and b is same object.
    * 'Slice operator' will create a new list, you can use `t[1:]` to create new list reference.
12. Debug
    * 大部分的方法都會影響原本list的內容，並且回傳`None`。
    * 挑選一種慣用方法(idiom)，並且一律使用這方法。
    * 注意適當的時機使用方法，由於會影響list的參考，所以視情況製作副本是必要的(可用'slice operator'產生副本)。