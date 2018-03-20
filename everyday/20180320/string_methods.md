# Python's string methods.
* Basic function: https://repl.it/@Traveler/Python-String-practice-All
* Methods: https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3


> ## Reference from [here](https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3)
> 1. join(): The str.join() method will __concatenate two strings__, but in a way that passes one string through another.
> 2. split(): The str.split() method __returns a list of strings__ that are separated by whitespace if no other parameter is given.
> 3. replace(): The str.replace() method can take an original string and __return an updated string with some replacement__.

## string_other.py
```python
def print_str_methods(text='Hello world, my name is John.'):
    # Concatenate the string to specify a character.
    print(' '.join(text))
    # Convert list to string.
    print(','.join(["01", "02", "03"]))
    # Replace to specify substring to new substring.
    print(text.replace("has","had"))
```
