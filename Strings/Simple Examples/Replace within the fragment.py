# Given a string. Replace every occurrence of the letter h by the letter H, except for the first and the last ones.

s = input()
s1=s[:s.find("h")+1]
s2=s[s.find("h")+1:s.rfind("h")]
s3=s[s.rfind("h"):]
s2=(s2.replace('h', 'H'))

print(s1+s2+s3)