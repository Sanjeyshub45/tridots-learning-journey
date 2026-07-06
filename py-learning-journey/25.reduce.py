### reduce
from functools import reduce
# nums = [1,2,3,4]
# total = reduce(lambda a,b : a+b,nums)
# print(total)
#1,2,3,4
#3,3,4
#6,4
#10

nums = [28,29,36,29,11,39,32,75,27,88,63,45,23]
find_max = reduce(lambda a,b : a if a>b else b,nums )
print(find_max)
#28,29 : 29
#29:36 : 36
#.
#.
#.
#88:23 : 88



#reduce(function,iterable)