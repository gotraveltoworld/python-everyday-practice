# think python 習題 19-1 p252
改寫以下方法(binomial_coeff)，二項式係數計算
* 練習範例： https://repl.it/@Traveler/Practices-19-1-binomialcoeff

```python
import time

n = 20
k = 20

start = time.time()
# Origin Example
def binomial_coeff(n, k):
    """Computer the binomial coefficient "n choose k".
        n: number of trials
        k: number of successes

        return: int
    """
    if k == 0:
        return 1
    if n == 0:
        return 0

    return binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)

print(binomial_coeff(n, k))
end = time.time()
elapsed = end - start
print('origin : K:%s-N:%s , Sec:%g' % (k , n, elapsed))

start = time.time()
# 用條件式改寫
def binomial_coeff(n, k):
    if k == 0:
        return 1
    elif n == 0:
        return 0
    else:
        return binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
print(binomial_coeff(n, k))
end = time.time()
elapsed = end - start
print('Condition : K:%s-N:%s , Sec:%g' % (k , n, elapsed))

start = time.time()
# 用memos換取計算時間
memos_dict = {(0, 0): 0}
def binomial_coeff(n, k):
    if k == 0:
        return 1
    elif n == 0:
        return 0
    elif (k, n) in memos_dict:
        return memos_dict[(k, n)]

    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    memos_dict[(k, n)] = res
    return res
print(binomial_coeff(n, k))
end = time.time()
elapsed = end - start
print('Memos method : K:%s-N:%s , Sec:%g' % (k , n, elapsed))

# origin : K:20-N:20 , Sec:1.4182
# Condition : K:20-N:20 , Sec:1.29618
# Memos method : K:20-N:20 , Sec:0.00088644
```