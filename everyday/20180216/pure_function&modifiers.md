# Python class practice

1. Pure function & modifiers
    - Pure function: 表示不會影響外部參數，並且會有回傳值。
    - Modifiers: 會影響外部的參數，直接修改傳入的引數(For example: 傳入物件就是傳參考位址而非值)
2. Prototype and patch: 製作原型後再補強。
    - 盡可能優先採取Pure function的方式進行開發
    - 必要時用Modifiers的方法來補足部分功能

練習範例：https://repl.it/@Traveler/Python-Class-example-4
```python
# 引用至example3, class: Time
class Time:
    """Show current timestamp

    attribute: hour, minute, second
    """
    hour = 10
    minute = 20
    second = 30

    # Support the print(class) method.
    def __str__(self):
        return self.time_format()

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_format(self):
        hour = '%.2d' % self.hour
        minute = '%.2d' % self.minute
        second = '%.2d' % self.second
        return '{0}:{1}:{2}'.format(hour, minute, second)

    def print_time(self):
        print(self.time_format())

# Create a simple pure function.
def add_time(t1, t2):
    sum_time = Time()
    time_unit = ['hour', 'minute', 'second']
    for t in time_unit:
        # Get the class's attribute by getattr()
        # Set the class's attribute by setattr()
        setattr(sum_time, t, getattr(t1, t) + getattr(t2, t))
    while sum_time.second > 60 or sum_time.minute > 60:
        if sum_time.second > 60:
            sum_time.second -= 60
            sum_time.minute += 1

        if sum_time.minute > 60:
            sum_time.minute -= 60
            sum_time.hour += 1

        if sum_time.hour > 24:
            return None

    return sum_time

# Test add_time function. For example,
# 1. sart
# 2. during time
# 3. Second and minute limit 60 and the hour limit 24.
start = Time()
start.set_time(9, 10, 55)

during = Time()
during.set_time(1, 40, 55)

end = add_time(start, during)
end.print_time()

```
