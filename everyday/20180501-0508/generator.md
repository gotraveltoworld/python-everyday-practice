# Python generator & yield expression

### Practice on repl.it(https://repl.it/@Traveler)
[generator repl.it](https://repl.it/@Traveler/py_generator)

## 前言
本文簡單描述關於python generator的相關用法和定義。
首先會稍微提到一些 ___iterator___ 相關的基本定義和物件的行為，然後根據 ___iterator___ 的方法，討論 ___generator___ 的行為。

### 迭代物件( ___Iterator___ )的基本定義

一個可迭代(iterable)的物件，可以用`for ... in ...`的語法實現迭代過程。實際就是呼叫物件中的`iter()`方法取得一個 ___iterator___ 。然後呼叫`next()`方法取得下一個元素的資料，直到結尾的例外出現為止(`StopIteration`)，這時`for... in ...`會自行處理結尾出現的例外事件。

```python
items = [1, 2, 3, 4, 5]
for r in items:
    print(r)
# 1. convert items to iterator
# 2. call the next
# 3. get the value
# 4-1. if value is not empty, return value.
# 4-2. if value is empty, return Exception StopIteration.
```
由上述就粗略可已知道iterator的運作方式，而在python中，任何有實現`__iter__()`和`__next__()`都可以稱為 ___iterator___ 。而 ___generator___ 即是 ___iterator___ 的一種實現方式。

### 生成器( ___Generator___ )的基本定義

引用自官方文件：
>  ___generator___ : A function which returns a generator iterator. It looks like a normal function except that it contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the ___next()___ function.
>
生成器或稱產生器( ___Generator___ )，是一種回傳產生器的函式，包含關鍵字 ___yield___ 表示式的一種函式。可用於`for ... in ...`語法中實現迭代，並且回傳`next()`方法藉此取得下一個元素。

同時，生成器也是一種惰性評估的函式(lazy evaluation of a function)，屬於函式編程範式的一種，主要是針對無法確切獲得的大量資料而設計的一種存取方式。也是一種迭代器( ___iterator___ )，具有可迭代(iteration)的性質。

> 迭代就是反覆回傳計算結果的一種運作方式，其目的是為了接近最終目標。每一次運算的過程就稱之為迭代(iterate)，藉由每次運算的結果，會將結果傳給下一次迭代。
---
在python中，就是用`for ... in ...`的語法實現迭代過程。由於python所有變數都是物 件，因此，只要該物件有實現`__iter__`方法，就可以進行迭代。可迭代的物件我們稱之為可迭代對象(iterable object)。
可迭代對象(iterable object)包含兩種類型，一種就是產生器( ___generator___ )，一種就是一般使用的列表(list)。

> 這兩者主要差異如下：
> 1. 列表會把所有資料存在記憶體中，以方便隨時存取，這種方式可以在記憶體中持續存取資料。缺點就是當資料量極大時，會使用列表存取速度極慢，而且有可能造成記憶體溢位。
> 2. 生成器實現惰性評估的方式，只評估最大數量。並且提供`next()`方法取用下一個元素。只有當呼叫`next()`方法時，才會回傳真實資料。可有效降低瞬間的記憶體用量。缺點是如果該資料會在應用中需要不只一次進行迭代作業時，就無法重用此資料。
> 3. 由於生成器有狀態，而列表並無狀態。所以實質上在進行迭代作業後，會有顯著的不同。

### 生成器( ___Generator___ )產生方式的範例程式碼
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

3. Use __yield__ expression.
```python
# (1)
def yield_example():
    yield 'Step 1'
    yield 'Step 2'
    print('Step 3')

generator = yield_example()
print(next(generator)) # Step 1
print(next(generator)) # Step 2
print(next(generator)) # StopIteration <= is empty.

# (2) from official(python), This is an example to lazily generate the prime numbers:
from itertools import count

def generate_primes(stop_at=0):
    primes = []
    for n in count(2):
        if 0 < stop_at < n:
            return # raises the StopIteration exception
        composite = False
        for p in primes:
            if not n % p:
                composite = True
                break
            elif p ** 2 > n:
                break
        if not composite:
            primes.append(n)
            yield n
```

### Reference
1. [wiki-python](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Generators)
2. [Generator and yield](http://kissg.me/2016/04/09/python-generator-yield/)
3. [Python syntax semantics](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Functional_programming)