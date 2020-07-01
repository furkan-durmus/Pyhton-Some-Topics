# 1. Strings
""" print('>_< ' * 5)  # >_< >_< >_< >_< >_<

print(len('abcdefghijklmnopqrstuvwxyz'))  # 26


s = str(2 ** 100)
print(s)  # 1267650600228229401496703205376
print(len(s))  # 31

"""

# 2. Slices: single character
"""
A slice gives from the given string one character or some fragment: substring or subsequence.

There are three forms of slices. The simplest form of the slice: a single character slice S[i] gives ith character of the string. We count characters starting from 0. That is, if S = 'Hello', S[0] == 'H', S[1] == 'e', S[2] == 'l', S[3] == 'l', S[4] == 'o'. Note that in Python there is no separate type for characters of the string. S[i] also has the type str, just as the source string.

Number i in S[i] is called an index.

If you specify a negative index, then it is counted from the end, starting with the number -1. That is, S[-1] == 'o', S[-2] == 'l', S[-3] == 'l', S[-4] == 'e', S[-5] == 'H'.
"""

# 3. Slices: subsequence
"""
s = 'abcdefg'
print(s[1])  # a
print(s[-1]) # g
print(s[1:3]) # bc
print(s[1:-1]) # bcdef
print(s[:3]) # abc
print(s[2:]) # cdefg
print(s[:-1]) # abcdef
print(s[::2]) # aceg
print(s[1::2]) # bdf
print(s[::-1]) gfedcba
"""

# 4. String methods: find() and rfind()
"""
s = 'Hello'
print(s.find('e'))
# 1
print(s.find('ll'))
# 2
print(s.find('L'))
# -1

#Similarly, the method rfind() returns the index of the last occurrence of the substring.

s = 'abracadabra'
print(s.find('b'))
# 1
print(s.rfind('b'))
# 8


#

s = 'my name is bond, james bond, okay?'
print(s.find('bond'))
# 11
print(s.find('bond', 12))
# 23
"""

# 5. String methods: replace()
"""
print('a bar is a bar, essentially'.replace('bar', 'pub'))
# 'a pub is a pub, essentially'

print('a bar is a bar, essentially'.replace('bar', 'pub', 1))
# 'a pub is a bar, essentially'
"""

#6. String methods: count()
"""
print('Abracadabra'.count('a'))
# 4
print(('aaaaaaaaaa').count('aa'))
# 5
print('0123se678se12se'.count('se',6,11))
# 1
"""

