# 條件式和遞迴

1. 下取除法(floor division)
    * 只取整數
2. 模數(modulus)
    * 回傳餘數
    * 可用於判斷兩數之間是否整除
    * 可用於取得單一數字最右邊的位數
        - `x % 10` 取得右邊一位
        - `x % 100` 取得右邊兩位

## conditions.py

```python
def print_first():
    mins = 100
    print(mins / 60)  # 1.6666666666666667 <= decimal parts.
    print(mins // 60) # 1 (Only int)
    print(mins % 60) # 40 (modulus operator), 回傳餘數
```