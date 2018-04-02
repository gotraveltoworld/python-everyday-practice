import sys
sys.path.append(sys.path[0])
fin = open('{0}\words.txt'.format(sys.path[0]))

# 當英文單字中沒有包含特定字母時回True
def has_no(word='', alphabet='e'):
    if alphabet not in word:
        return True
    else:
        return False

total = 0
e_number = 0
for f in fin:
    if has_no(f):
        e_number += 1# Has no 'e'
    else:
        pass # Skip
    total += 1

percentage = '{0!s:.6}%'.format((e_number / total) * 100)
print(percentage)

# other solution(list comprehension).
fin = open('{0}\words.txt'.format(sys.path[0]))
e_number = len([f for f in fin if has_no(f)])
fin = open('{0}\words.txt'.format(sys.path[0]))
total = len([f for f in fin])
percentage = '{0!s:.6}%'.format((e_number / total)* 100)
print(percentage)

