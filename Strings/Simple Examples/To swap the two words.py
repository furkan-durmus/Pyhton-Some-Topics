# Given a string consisting of exactly two words separated by a space.
# Print a new string with the first and second word positions swapped (the second word is printed first).
# This task should not use loops and if.

s = input()
print(s[s.find(" ")+1:],s[:s.find(" ")])