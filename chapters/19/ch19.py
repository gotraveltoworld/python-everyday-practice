"""
    用條件判斷式讓程式更簡潔
"""

# conditional expression
# Example 1-1
# Check the args defaul plot

def check_before(x):
    if x:
        return x
    else:
        return False

def check_after(x):
    return x if x else False

# Print result.
input = 100
print('check_before', check_before(input))
print('check_after', check_after(input))



"""
    用串列概括式讓List處理的更簡潔
"""

# Reference "https://openhome.cc/Gossip/Python/ForComprehension.html"
#  Example 2-1
scores = [('Justin', 95), ('momor', 93), ('Hamimi', 99)]
print({name : score for (name, score) in scores})

#  Example 2-2, Create one list of two string combinations.
print([letter1 + letter2 for letter1 in 'Justin' for letter2 in 'momor'])

# Examnple 2-3, Two dimensions list convert to one dimension list.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print([element for row in matrix for element in row])

# Other example.
# According to the specified key to filter all duplicate elements.
db_iter = [ {'id': 1}, {'id': 1}, {'id': 2} ]
print({row.get('id'): row for row in db_iter if row.get('id', None)})

