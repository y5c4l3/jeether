# Incorrect optimization in itertools.tee() #123884
# https://github.com/python/cpython/issues/123884

# Original PoC:
"""
from itertools import tee

def demo(i):
    it = iter('abcdefghi')
    [outer_tee] = tee(it, 1)
    inner_tee = tee(outer_tee, 10)[i]
    return next(inner_tee), next(outer_tee)

print('These should all give the same result:')
for i in range(10):
    print(i, demo(i))
"""

from itertools import tee, cycle

simple = iter('abcd')
f = open('/proc/self/status') # a randomly picked file in procfs
simple_tees = tee(simple, 10)
file_tees = tee(f, 10)
print(next(simple))
print(list(map(lambda it: next(it), simple_tees)))
print(next(f))
print(list(map(lambda it: next(it), file_tees)))

def parsenum(it):
    it, peek = tee(it)
    num = ''
    while next(peek).isdigit():
        num += next(it)
    return it, int(num)

def parseword(it):
    it, peek = tee(it)
    word = ''
    while next(peek).isalpha():
        word += next(it)
    return it, word

it = iter('1234+abcd' * 1000)
tokens = []
while True:
    try:
        it, peek = tee(it)
        if next(peek).isdigit():
            it, num = parsenum(it)
            tokens.append(num)
            continue
        it, peek = tee(it)
        if next(peek).isalpha():
            it, word = parseword(it)
            tokens.append(word)
            continue
        it, peek = tee(it)
        if next(peek) in '+-*/':
            op = next(it)
            tokens.append(op)
            continue
    except StopIteration:
        break

print(tokens)
