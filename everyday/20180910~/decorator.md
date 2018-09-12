# Python decorator.

## 前言
python decorator的概念

python decorator 的概念是基於python可以將函式當作參數進行傳遞的原則上實作的一種模式。

先理解函式可以像是參數傳遞一樣，在每一個函式中傳遞，例如：
```python
def one(func):
    func()

def two():
    print('print one')

one(two) # print one
```
其本質上是一個python的類別或是函式，可以在不需要修改原始碼的情況下增加額外功能。其回傳也是一個函式或是類別。常用於：紀錄日誌、性能測試、快取服務以及身分驗證等相關應用。用decorator這種設計方式，可以有效的抽離跟函式本身功能無關的其他附加功能，並且可以按照需求添加其他功能。
例如，新增一筆輸出：
```python
def one(func):
    print('print one')
    print('print: I am a L') # 假設這句話要在很多地方出現，就需要在每一個函式裡面加入這項命令。

def two():
    print('print two')
    print('print: I am a L') # 假設這句話要在很多地方出現，就需要在每一個函式裡面加入這項命令。
```
這種時候就會產生非常大量的一模一樣或是相似的程式片段在每一個函式中出現，因此，這種時候可以選用`decorator`來處理這樣的情形。
例如：
```python
def print_L(func):
    print('print: I am a L')
    func()

def one():
    print('print one')

print_L(one)
# print: I am a L
# print one
```

### 簡單裝飾器
但是這樣的結果就是呼叫的時候會改用`print_L`來呼叫，導致後續的功能都需要因為新增的功能而全部修正呼叫方式。這會破壞原有的結構，所以我們可以選用`decorator`的方式來實作。
```python
# simple_decorator
def print_L(func):
    def wrapper():
        print('print: I am a L')
        return func()   # 把 one 做為參數來傳遞，執行func()就是執行one()
    return wrapper

def one():
    print('print one')

one = print_L(one)  # Decorator print_L(one) 回傳 wrapper，實際就是  one = wrapper
one()               # one() = wrapper()
```

### 語法糖
也可以用語法糖的方式來實現：
```python
# syntax_sugar_decorator
def print_L(func):
    def wrapper():
        print('print: I am a L')
        return func()
    return wrapper

@print_L
def one():
    print('print one')

one()
```
用了`@`可以不需要賦值的指令，直接呼叫`one()`來獲得我們要的結果。

### 類別型裝飾器
裝飾器也可以用類別來實現，實現方式就是利用`__call__`的方法來實作。
```python
class One(object):
    def __init__(self, func):
        self._func = func
    # __call__ 被呼叫的函式
    def __call__(self):
        print ('One Runing')
        self._func()
        print ('One Ending')

@One
def two():
    print ('print two')

two()
```

### 裝飾器執行順序
```python
@a
@b
@c
def fun():
    pass

# 執行順序是從裡到外，最先呼叫最裡層的裝飾器，最後才呼叫最外層的裝飾器
fun = a(b(c(fun)))
```
### 類別包裝裝飾器
在類別中運用裝飾器的例子。
```python
class Filter_Text:

    def filter_one(fun):
        def wrapper(self, text=''):
            result_text = fun(self, text)
            return result_text

        return wrapper

    def filter_two(fun):
        def wrapper(self, text=''):
            result_text = fun(self, text)
            return result_text
        return wrapper

    @filter_one
    @filter_two
    def filtet_text(self, text=''):
        return text
```

