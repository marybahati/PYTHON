Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=1,2,3
>>> b=4,5,6
>>> c=7,8,9
>>> flat=[x for x in a+b+c]
>>> flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> 
>>> 
>>> squares=[x*x for x in flat]
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
