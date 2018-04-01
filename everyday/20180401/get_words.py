import sys
sys.path.append(sys.path[0])
fin = open('{0}\words.txt'.format(sys.path[0]))

# 印出超出特定字元的單字
def get_specify_len(word='', length=20):
    if len(word) > length:
        return '{0!r}'.format(word)
    else:
        return ''

# 當英文單字中沒有包含特定字母時回True
def has_no(word='', alphabet='e'):
    if alphabet not in word:
        return True

for f in fin:
    word = get_specify_len(f, length=20)
    if word and has_no(word):
        print(word)
        # 'microminiaturization\n'
        # 'microminiaturizations\n'



