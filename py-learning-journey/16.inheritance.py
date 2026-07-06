#single inheritance:
# class dad: #parent
#     def house(self):
#         print("I am from dad house")
# class son(dad): #child
#     def factory(self):
#         print("I am from factory")

# s = son()
# s.house() #inherited

#Multiple Inheritance (child inherits more than one parent)
# class p1: #parent 1
#     def f1(self):
#         print("Feature_1")
# class p2: #parent 2
#     def f2(self):
#         print("Feature_2")
# class c1(p1,p2): #inherited 2 parents
#     pass
# obj = c1()
# obj.f1()
# obj.f2()


#Multilevel Inheritance (one class inherits another class which also inherits another class ,that maked multiple level):
# class gp:
#     def mes1(self):
#         print("Inherited GrandFather")
# class p(gp):
#     def mes2(self):
#         print("Inherited Parent")
# class c(p):
#     def mes3(self):
#         print("Inherited child")
# obj = c()
# obj.mes1()
# obj.mes2()
# obj.mes3()


#Hierarchical Inheritance:(more than one class inherits single  same class)
# class P:
#     def mes_p(self):
#         print("I am Parent...")
# class C1(P):
#     def mes_c1(self):
#         print("I am child 1...")
# class C2(P):
#     def mes_c2(self):
#         print("I am child 2...")
# obj1 = C1()
# obj1.mes_p()
# obj2 = C2()
# obj2.mes_p()

##Hybrid Inheritance is a combination of one or more inheritance.
