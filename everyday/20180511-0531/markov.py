import sys
import random

global words
global words_map
words = ()
words_map = {}
def markov_analysis(word='', ord=2):
    global words
    global words_map
    if (len(words) < ord and word):
        words += (word,)

    if words_map.get(words):
        # if there is an entry, to add new item.
        words_map[words].append(word)
    else:
        # if there is no entry for this prefix, make one.
        words_map[words] = [word]

    # Forms a new tuple by removing the head and adding word to the tail.
    words = shift(words, word)

def read_file(filename='emma.txt', order=2):
    """Read file to analyse any sentences.

    filename: string
    order: integer number of words in the prefix

    returns: map from prefix to list of possible suffixes.
    """
    with open(filename) as fin:
        for f in fin:
            # Skip the header page.
            if f.startswith('*END*THE SMALL PRINT!'):
                continue
            for word in f.rstrip().split():
                markov_analysis(word)

def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)


def random_text(n=10):
    """Generates random wordsfrom the analyzed text.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = random.choice(list(words_map.keys()))

    for i in range(n):
        suffixes = words_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n-i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        print(word, end=' ')
        start = shift(start, word)

def main(script, filename='emma.txt', n=100, order=2):
    try:
        n = int(n)
        order = int(order)
        read_file(filename, order)
        random_text(n)
    except ValueError:
        print('Usage: %d filename [# of words] [prefix length]' % script)

if __name__ == '__main__':
    main(*sys.argv)