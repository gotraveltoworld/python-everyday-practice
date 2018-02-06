# any 和 all 練習
1. any : 接受一個序列的參數，其中之一符合就回傳True。
2. all : 接受一個序列的參數，所有資料都符合才會回傳True。


* 練習範例： https://repl.it/@Traveler/Python-any-and-all
```python
# any example.
arr = [True, False, True]
ex1 = any(arr)
print('any', ex1)

# all example
ex1 = all(arr)
print('all', ex1)
```
# any and generator(From book example)
```python
res = any(letter == 't' for letter in 'monty')
print(res)
```

```python
# Practice 1
# word = Jack
# 可以用在比較字串，以下的方法只允許沒有在'forbidden'裡面的字串。
def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)

print('Allow:', avoids('Jack', 'b'))
print("Don't allow:", avoids('Jack', 'a'))

# Practice 2
word = """
    Nice too meet you.
    My name is Jack.
    And I am an software engineer.
"""
# 用all改寫以下方法(檢查字串是不是用到所有的母音aeiou)
def uses_all(word, vowels='aeiou'):
    for vowel in vowels:
        if not vowel in word:
            return False
    return True

print('uses_all:', uses_all(word))

# from for loop to all method
def uses_all(word, vowels='aeiou'):
    return all(vowel in word for vowel in vowels)

print('uses_all:', uses_all(word))
```