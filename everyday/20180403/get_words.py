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

print(allows, uses, needs, needs_v2)


