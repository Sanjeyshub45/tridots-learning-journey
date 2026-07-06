#higher order functions is a type of function wich able to take another function as an argument or return an function as output.used to make flexible code,resubale,dynamic.

#1.function as an argument
# def gmail_creator(username,domain="gmail.com"):
#     return f"{username}@{domain}"
# def yahoo_creator(username,domain="yahoo.com"):
#     return f"{username}@{domain}"
# def hotmail_creator(username,domain="hotmail.com"):
#     return f"{username}@{domain}"
# def build_email(username,email_func):
#     return email_func(username)

# print(build_email("sanjey",gmail_creator))
# print(build_email("sanjey",yahoo_creator))
# print(build_email("sanjey",hotmail_creator))

#function returns another function:--

# def domain(domain_name):
#     def assign_email(name):
#         return f"{name}@{domain_name}"
#     return assign_email

# gmail =  domain("gmail.com")
# print(gmail("sanjey"))



