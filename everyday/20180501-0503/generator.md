# Python generator

### Practice on repl.it(https://repl.it/@Traveler)
[generator repl.it](https://repl.it/@Traveler/py_generator)

生成器或稱產生器(Generator)，是一種惰性評估的函式(lazy evaluation of a function)，屬於函式編程範式的一種，主要是針對無法確切獲得的大量資料而設計的一種存取方式。也是一種迭代器(iterator)，具有可迭代(iteration)的性質。

> 迭代就是反覆回傳計算結果的一種運作方式，其目的是為了接近最終目標。每一次運算的過程就稱之為迭代(iterate)，藉由每次運算的結果，會將結果傳給下一次迭代。
---
在python中，就是用`for ... in ...`的語法實現迭代過程。由於python所有變數都是物 件，因此，只要該物件有實現`__iter__`方法，就可以進行迭代。可迭代的物件我們稱之為可迭代對象(iterable object)。
可迭代對象(iterable object)包含兩種類型，一種就是產生器(generator)，一種就是一般使用的列表(list)。

> 這兩者主要差異如下：
> 1. 列表會把所有資料存在記憶體中，以方便隨時存取，這種方式可以在記憶體中持續存取資料。缺點就是當資料量極大時，會使用列表存取速度極慢，而且有可能造成記憶體溢位。
> 2. 生成器實現惰性評估的方式，只評估最大數量。並且提供`next()`方法取用下一個元素。只有當呼叫`next()`方法時，才會回傳真實資料。可有效降低瞬間的記憶體用量。缺點是如果該資料會在應用中需要不只一次進行迭代作業時，就無法重用此資料。
> 3. 由於生成器有狀態，而列表並無狀態。所以實質上在進行迭代作業後，會有顯著的不同。

### Example
1. Basic principle.
```python
# Show all iter elements.
def for_loop(arr):
    for a in arr:
        print(a)

arr = [1, 2, 3]
arr_it = iter([4, 5, 6])
for_loop(arr)
for_loop(arr_it)
print('--------')
for_loop(arr)
for_loop(arr_it) # <= nothing result, because this iter is StopIteration.
```
2. Generator expressions.
```python
# generator expressions
x_iter = (x for x in range(5))
print(x_iter)
# <generator object <genexpr> at 0x7fd7339355c8>
for x in x_iter:
    print(x)
    # 0 - 4

print(next(x_iter))
# Traceback (most recent call last): File "python", line 5, in <module>
# StopIteration
```


### Reference
1. [wiki-python](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Generators)
2. [Generator and yield](http://kissg.me/2016/04/09/python-generator-yield/)