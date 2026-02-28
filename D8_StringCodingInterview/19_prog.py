#WAP to find the no/- of occurance of each vowel present in the string?
# 2 strings are said to be anagrams iff both are having ame content irrespective of charater position
# ex: lazy = zaly, listen = silent, triangle = integral

s1= input("enter 1st string:")
s2=input("enter 2nd string:")
if (sorted(s1) == sorted(s2)):
    print("the 2 strings are anagrams")
else:
    print("the 2 strings are not anagrams")