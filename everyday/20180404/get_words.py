import sys
sys.path.append(sys.path[0])
fin = open('{0}\words.txt'.format(sys.path[0]))

# 9-3 avoids
def avoids(word, forbiddens=''):
    for w in word:
        if w in forbiddens:
            return False
    return True
# 9-4 uses_only
def uses_only(word, available=''):
    for w in word:
        if w not in available:
            return False
    return True
# 9-5 uses_all
def uses_all(word, required=''):
    for w in required:
        if w not in word:
            return False
    return True

# 9-5 uses_all by uses_only
def uses_all_v2(word, required=''):
    return uses_only(required, word)


# 9-6 abecedarian
# version 1, indices(index)
def is_abecedarian_v1(word=''):
    previous = word[0] if len(word) > 0 else ''
    for w in word:
        if w < previous:
            return False
        previous = w
    return True
# version 2, recursion.
def is_abecedarian_v2(word=''):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_v2(word[1:])
# version 3, while loop.
def is_abecedarian_v3(word=''):
    i = 0
    while i < (len(word) - 1):
        if word[i+1] < word[i]:
            return False
        i = i + 1
    return True

# Import from 20180227
def is_reverse(word1, word2):
    # Guardian pattern.
    if len(word1) != len(word2):
        return False

    i = 1
    for w1 in word1:
        if w1 != word2[-i]:
            return False
        i += 1
    return True
# Import from 20180228
def is_palindrome(word):
    return is_reverse(word, word)

print('Please, input your string of forbidden letters')
# forbiddens = input('input: ')
forbiddens = 'aeiou'
available = 'aeiou'
required = 'aeiou'

total = 0
allows = 0
uses = 0
needs = 0
needs_v2 = 0
abecedarian_v1 = 0
abecedarian_v2 = 0
abecedarian_v3 = 0
is_palind = 0
for f in fin:
    total += 1
    word = f.strip()
    if avoids(word, forbiddens):
        allows += 1 # No forbidden letters.

    if uses_only(word, available):
        uses += 1 # Uses only.

    if uses_all(word, required):
        needs += 1

    if uses_all_v2(word, required):
        needs_v2 += 1

    if is_abecedarian_v1(word):
        abecedarian_v1 += 1
    if is_abecedarian_v2(word):
        abecedarian_v2 += 1
    if is_abecedarian_v3(word):
        abecedarian_v3 += 1

    if is_palindrome(word):
        print(word)
        is_palind += 1

print(allows, uses, needs, needs_v2)
print(abecedarian_v1, abecedarian_v2, abecedarian_v3)
print('is_palindrome:', is_palind)