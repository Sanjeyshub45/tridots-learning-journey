#ability of method to behave differently in different situtation:\
#There is no method overloading in pYthon,overriding is in python
class add_v1():
    def add(self,a,b):
        print(a+b)
class add_v2(add_v1):
    def add(self,a,b): #overriding add method
        print("The Result is :",a+b)
obj = add_v2()
obj.add(99,1)