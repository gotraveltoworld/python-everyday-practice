# Python's string format.
* Basic function: https://repl.it/@Traveler/Python-String-practice-All

# Record some fo source codes from official site.

```python
# Python 3.6
# https://docs.python.org/3.6/library/string.html#format-examples
import datetime

def official_example():
    # Basic.
    '{0}, {1}, {2}'.format('a', 'b', 'c')
    '{}, {}, {}'.format('a', 'b', 'c') # 3.1+ only
    '{2}, {1}, {0}'.format('a', 'b', 'c')
    '{2}, {1}, {0}'.format(*'abc') # unpacking argument sequence
    '{0}{1}{0}'.format('abra', 'cad') # arguments' indices can be repeated
    # => 'abracadabra'

    # Keys and unpacking dict.
    'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
    coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
    'Coordinates: {latitude}, {longitude}'.format(**coord)

    c = 3-5j
    ("""
        The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.
    """).format(c)
    # 'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'
    coord = (3, 5)
    'X: {0[0]};  Y: {0[1]}'.format(coord) # 'X: 3;  Y: 5'

    # r and s flag.
    "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
    # "repr() shows quotes: 'test1'; str() doesn't: test2"

    # format also supports binary numbers
    "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
    # 'int: 42;  hex: 2a;  oct: 52;  bin: 101010'

    # Using the comma as a thousands separator:
    '{:,}'.format(1234567890)
    # '1,234,567,890'

    # Expressing a percentage:
    'Correct answers: {:.2%}'.format(19/22)
    # 'Correct answers: 86.36%'


    d = datetime.datetime(2010, 7, 4, 12, 15, 58)
    '{:%Y-%m-%d %H:%M:%S}'.format(d)
    # '2010-07-04 12:15:58'

    # complex
    for align, text in zip('<^>', ['left', 'center', 'right']):
        '{0:{fill}{align}16}'.format(text, fill=align, align=align)
    """
        'left<<<<<<<<<<<<'
        '^^^^^center^^^^^'
        '>>>>>>>>>>>right'
    """

    octets = [192, 168, 0, 1]
    '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
    # 'C0A80001'
```