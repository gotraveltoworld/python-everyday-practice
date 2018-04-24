# Python dict practice.
### Link: https://repl.it/@Traveler/dictfunctions

## Practices
1. 11-1: 讀取words.txt，儲存所有文字作為鍵值，並用`in`運算子檢查是否在字典中。
```python
import sys
sys.path.append(sys.path[0])
fin = open('{0}/words.txt'.format(sys.path[0]))

for f in fin:
    key = '{0}'.format(f.strip())
    dic[key] = ''
if 'aa' in dic:
    print('aa') # aa
else:
    print('No')
```
2. 11-2 用`setdefault`改寫‵`invert_dict`方法
    ```python
    def invert_dict_adv(dic = {}):
        """Inverts a dictionary, returning a map from val to a list of keys.
        反轉字典，並回傳一個由val映射到鍵值的列表
        """
        inverse = {}
        for key in dic:
            val = dic[key]
            # Convert new list.
            inverse.setdefault(val, []).append(key)
        return inverse
    ```
