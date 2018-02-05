# 練習產生器運算式(generator expressions)
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
產生器跟串列都可以用for進行迭代(iterate through)

基本差異：
1. 產生器是藉由next調用後才會取得下一個值
2. 當到達尾端時會回傳"StopIteration"例外

* 常與 sum, max, min之類的方法一起使用。