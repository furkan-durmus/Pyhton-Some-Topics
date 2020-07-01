# Given a string. Cut it into two "equal" parts (If the length of the string is odd, place the center character in the first string,
# so that the first string contains one more characther than the second).
# Now print a new string on a single row with the first and second halfs interchanged (second half first and the first half second)
# Don't use the statement if in this task.

s = input()
print(s[len(s)//2+len(s)%2:]+s[:len(s)//2+len(s)%2])