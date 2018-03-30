# Incremental development 漸進式開發練習

## 目標：藉由簡單的習題練習漸進開發的邏輯。
    1. Scaffolding(鷹架)：包含print輸出。
    2. 由處理的問題先行勾勒原型。

## 練習的題目：計算畢氏定理，兩點之間的距離。
` distance = sqrt((x2 -x1) **2 + (y2 - y1) **2))`
## Step
1. 輸入四個變數 `x1, x2, y1, y2`
2. 建立基本算式：
    - 基本減法：`x2 - x1, y2 - y1`
    - 平方：`(x2 - x1) **2, (y2 - y1) **2`
    - 平方根； `math.sqrt((x2 - x1) **2 + (y2 - y1) **2)`
3. 各步驟輸出：
    - `print(x2 - x1)`
    - `print((x2 - x1) **2)`
    - `print(math.sqrt((x2 - x1) **2) + (y2 - y1) **2))`

```python
import math
# Step 1, Set all parameters.
def distance(x1, x2, y1, y2):
    return 0.0
# Step 2, Add the subtract formula, and to save in temporary variable.
def distance(x1, x2, y1, y2):
    x = x2 - x1
    y = y2 - y1
    print(x, y)
# Step 3, Add the squares(sum of squares)
def distance(x1, x2, y1, y2):
    x = x2 - x1
    y = y2 - y1
    sum_of_squares = (x **2) + (y **2)
    print(sum_of_squares)
# Step 4, Final add the return result.
def distance(x1, x2, y1, y2):
    x = x2 - x1
    y = y2 - y1
    sum_of_squares = (x **2) + (y **2)
    result = math.sqrt(sum_of_squares)
    print(result)
    return result
# Complete the distance function.
def distance(x1, x2, y1, y2):
    x = x2 - x1
    y = y2 - y1
    sum_of_squares = (x **2) + (y **2)
    result = math.sqrt(sum_of_squares)
    return result
```