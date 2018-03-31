import sys
sys.path.append(sys.path[0])
fin = open('{0}\words.txt'.format(sys.path[0]))
print('{0!r}'.format(fin.readline()))