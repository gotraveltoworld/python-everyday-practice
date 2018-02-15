# Python class practice

1. function in class
2. __str__ for class debug.
3. According to the book example to check time range.

```python
class Time():
    """Show current timestamp

    attribute: hour, minute, second
    """
    hour = 10
    minute = 20
    second = 30

    # Support the print(class) method.
    def __str__(self):
        return self.time_format()

    def time_format(self):
        hour = '%.2d' % self.hour
        minute = '%.2d' % self.minute
        second = '%.2d' % self.second
        return '{0}:{1}:{2}'.format(hour, minute, second)

    def print_time(self):
        print(self.time_format())

# Create time
t = Time()
t.hour = 1
t.minute = 10
t.second = 20

t.print_time()
# Test print method.
print('Test __str__:', t)

# is_after, 時間比較。
def is_after(t_after, t_before):
    after = int(t_after.hour * 60 * 60 +
                    t_after.minute * 60 +
                        t_after.second)
    before = int(t_before.hour * 60 * 60 +
                    t_before.minute * 60 +
                        t_before.second)

    return True if after > before else False

t1 = Time()
t1.hour = 12
t1.minute = 10
t1.second = 20
t1.print_time()
t2 = Time()
t2.hour = 11
t2.minute = 10
t2.second = 20
t2.print_time()
print(is_after(t1, t2))
```