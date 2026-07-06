#Local - Enclosed - Global - Built-in:

#Local:
# def order():
#     food = "rice"
#     print("Your Order:",food)

# order()
# print(food) #not going to print becoz of local scope (food is local variable for order func)

#Enclosing:
# def cart():
#     discount = 10
#     def checkout():
#         print("Obtained discount",discount)
#     checkout()
# cart()
#discount can be used to another func inside one func becoz in enclosing inner fumction can use their parent function var.

#Global:
# userId = "sanjey_001"
# def homepage():
#     print("Welcome:",userId)
# def profile():
#     print("Welcome to Profile page:",userId)
# homepage()
# profile()
#var can be used anywhere inside that py script

#Built-in:
# print(__file__)
#scope can handled by python and can used globally

# del_partner = "swiggy"
# def hotel():
#     item = "pizza"
#     def order():
#         qty = 2
#         print(f"Ordering Qunatity {qty}{item} using {del_partner}")
#     order()
# hotel()