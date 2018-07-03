# Python methods of class.

### Practice on repl.it(https://repl.it/@Traveler)
1. [PyClass](https://repl.it/@Traveler/PyClass)

## 前言
練習python相關的物件建立方法和一些介面實作，主要目的：
1. 練習class語法
2. 練習`static`和`class`方法
3. 參考設計模式，用python寫一些設計模式來模擬實務問題
4. 藉由此練習來改寫公司的python專案

### 基本說明
Python具有 [__物件導向__](https://zh.wikipedia.org/zh-tw/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1) (Object Oriented Programming, 簡稱OOP)的設計範式，因此也實現了一些OOP相關的特點：
* 封裝(Encapsulation): 隱藏部分變數和方法，使得外部成員能存取的資料是有限的。
* 繼承(Inheritance): 就像父子關係為例，子類別可以繼承父類別的一些特性。如同孩子會繼承父親一些特徵，在物件實現上就是子類別可以直接拿父類別的屬性和參數來使用，避免重複實作相同的功能。
* 多型(Polymorphism): 代表相同的行為有不同表示方法，如同狗和貓都繼承會叫的生物，但兩者之間的叫聲表現在外在完全不同。以物件來解釋就是繼承相同的方法，但各自實作細節。
* 抽象性(Abstraction): 表示在部分案例中，可以直接借用其他類別來實現後續的功能。例如：John是一隻豹，而我們有一個物件是代表貓，由於貓和豹兩者都是貓科動物，行為很像。所以如果要描述John這隻豹，可以直接用抽象類別的方式來描述John，基本上John在大多數都可以視作跟一隻貓。

基本上 __物件導向__ 是為了解決功能重複性而被廣泛使用。由於python所有一切都是物件，因此更了解 __物件導向__ 的概念會有助於了解程式的運作。

## 基礎語法和說明
### Class and Instance
類別是基本上就是一個封裝完成的抽象物件，其中包含屬性和方法。而實例就是一個具體的物件。
* 宣告語法: [參考](https://stackoverflow.com/questions/4015417/python-class-inherits-object)
FirstClass是類別名稱，一般而言是用大寫開頭，多字詞就是每個字詞首字都大寫。
### First Class
```python
"""Declare a one class object.
"""
class FirstClass:
    pass
```
### methods of Class
```python
"""Declare a one class object.
    These are some functions in the class.
"""
class FirstClass:

    def first_method(self):
        pass

    def second_method(self):
        pass
```
### create an instance
```python
"""Declare a one class object.
    These are some functions in the class.
"""
class FirstClass:

    def first_method(self):
        pass

    def second_method(self):
        pass

first_class = FirstClass()  # Create an instance
first_class.first_method()  # use the first_method()
first_class.second_method() # use the second_method()
```

### Initial function
```python
"""Declare a one class object.
    These are some functions in the class.
"""
class FirstClass:

    name = 'FirstClass'

    def __init__(self, name='FirstClass_init'):
        print('Show initial....')
        self.name = name
        pass

    def first_method(self):
        pass

    def second_method(self):
        pass

first_class = FirstClass()  # Create an instance, and to initial the name.
first_class.first_method()  # use the first_method()
first_class.second_method() # use the second_method()
print(first_class.name) # FirstClass_init
```

### Encapsulation(封裝)
```python
"""Use the basic function to demo the example.
"""
class ShowEncapsulation:
    name = 'public_name'
    _name = 'protest_name'
    __name = 'private_name'
    pass

print(ShowEncapsulation().name)
print(ShowEncapsulation()._name)
try:
    print(ShowEncapsulation().__name)
except Exception as e:
    print(e) #'ShowEncapsulation' object has no attribute '__name'

# To enforce to get the function of private.
print(ShowEncapsulation()._ShowEncapsulation__name) # private_name
```
重點：
1. python沒有硬性方法遮蔽從外部存取方法，一般是使用底線的方式來區別內部和外部屬性。
2. 目前只有使用雙底線屬性可以藉由內部更名的方式避開直接存取(仍然可以用其他方法存取)。
    - `_ShowEncapsulation__name`(_classname_attr)

### Inheritance(繼承)
```python
"""Declare an inheritance class.
"""
class ParentClass:

    name = 'FirstClass'

    def __init__(self, name='Parent_init'):
        print('Show initial of inheritance....')
        self.name = name
        pass

class ChildClass(ParentClass):

    def __init__(self, name='ChildClass_init'):
        super().__init__(name)
        pass

class_instance = ChildClass()  # Create an instance, and to initial the name.
class_instance.name  # show the parent's name.
'''
Show initial of inheritance....
ChildClass_init
'''
```
重點：
1. 用`super()`存取父類別的屬性和方法。
2. 子類別需要傳入父類別`ChildClass(ParentClass)`。
3. 根據實際需求設計物件之間的繼承關係，可以有效降低重複性的功能。
4. 繼承的類別可以利用覆寫(Over-write)特性來重新定義相同屬性或是方法。
    ```python
    class ParentClass:
        def show(self):
            print('Parent')

    class ChildClass(ParentClass):
        def parent_show(self):
            super().show()
        def show(self):
            print('Child')

    ChildClass().parent_show() # Parent
    ChildClass().show() # Child
    ```