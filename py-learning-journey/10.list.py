#maintains index based order,mutable (CRUD),store multiple dtypes
# fav_heros = ["vijay","ajith","karthik","vikram"]
# fav_heroines = ["Samantha","Kajal","Tamannah","Hansika"]
# fav_comedians = ["Santhanam","Vadivel","Vivek","Sathish"]
# print(fav_heros)
# print(fav_comedians)
# print(fav_heroines)

#list Menthods:
# num = [98,99,99]
# print(num)
# num.append(100) #append menthod appends at last
# print(num)
# num.insert(0,1000) #appens at partcular index
# print(num)
# num.remove(1000) #remove first occurence of value
# print(num)
# num.pop() #take last value
# print(num)
# num.reverse() # reverse entire list
# print(num)
# print(num.index(99)) #gives index of the passed value
# print(num.count(99)) # count the occurence of  passed value

#List Slicing:
# num = [1,2,3,45,5,4]
# print(num[0:2]) #[start:stop(stop run until stop-1):step]

#List iteration:
# num = [82,292,92,29,37]
# for i in num:
#     print(i)

#Chech item item exist in list:
# num = [33,32,46,56]
# if 99 in num:
#     print("Yes")
# else:
#     print("No")

# updating value at index
# num = [23,44,56,85]
# change = num.index(44)
# num[change] = 55
# print(num)

#enumerate in list:
# num =["Pizzz","Apple","Gun"]
# for i,item in enumerate(num):
#     print(f"{i}:{item}")