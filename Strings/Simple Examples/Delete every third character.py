# Given a string. Delete from it all the characters whose indices are divisible by 3.
s = input()

for i in range(len(s)):
    if i%3!=0:
        print(s[i],end="")