# 聚集不特定參數和關鍵字參數(`*arg`, `**kwargs`)
* `*arg` 和 `**kwargs`
* 練習範例： https://repl.it/@Traveler/Python

```python
# Set some args by parameters.
def args(*args):
    print(args)
args(1, 2, 3, 4, 5)

dict_one = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

def kwargs(**kwargs):
    print(kwargs)
kwargs(one=1, two=2, three=3, four=4, five=5)
kwargs(**dict_one)

def args_and_kargs(*args, **kwargs):
    print('arg: ', args)
    print('kwargs: ', kwargs)

args_and_kargs(1, 2, 3, 4, 5, **dict_one)
# arg:  (1, 2, 3, 4, 5)
# kwargs:  {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
```