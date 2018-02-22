# Python decorator method
### Target:
1. Test @decorator
2. Practice @decorator
    - decorator可以替換成其他函式
    - decorator在引入模組的階段就會執行(import stage)

Reference:
1. http://blog.gusibi.com/post/python-decorator/
2.

練習範例：https://repl.it/@Traveler/Python-decorator

實際執行是從
```python
"""First stage
1. Practice the decorator method
2. 用decorator修飾方法函式，會直接執行。
"""
def decorator(fn):
    print('Show function name {0}'.format(fn.__name__))

@decorator
def function():
    pass

# Result: Show function name function

# Check the decorator executing.
records = []  # registry 紀錄
def decorator_func(func):  # register 參數是函式
    print('Show records {0}'.format(func.__name__)) # Print fucntion name
    records.append(func)  # Save into 'records'
    return func  # 必須回傳函式

@decorator_func
def fun1():
    print('running {0}'.format(fun1.__name__))

@decorator_func
def fun2():
    print('running {0}'.format(fun2.__name__))

def fun3():
    print('running {0}'.format(fun3.__name__))

def run():
    print('decorator_func :', records)
    fun1()
    fun2()
    fun3()

run() # Run all test function
"""
Show records fun1
Show records fun2
decorator_func -> [<function fun1 at 0x7fa0d9225488>, <function fun2 at 0x7fa0d9225510>]
running fun1
running fun2
running fun3
--------------
總結：
1. 在run()之前就顯示Show records fun1以及Show records fun2，代表decorator直接運行的特性
2. 用decorator可以讓函式變成一個參數傳入其他函式。
"""

"""Second stage
1. 實現一個decorator模式的程式碼
2. 理解closure(閉包)的特性
    - 函式變數的作用域
    - 函式在閉包內的執行方式
"""
def decorator_example(func):
    def closure():
        print('Before run fucntion')
        func()
        print('After run function')
    return closure

@decorator_example
def test():
    print('Run test fucntion')

test()
"""Result:
Before run fucntion <- Before
Run test fucntion <- Main fucntion
After run function <- After
"""
```