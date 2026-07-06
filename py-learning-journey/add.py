def addOf(a,b):
    return a+b

def addOf(*arg):
    total = 0
    for num in arg:
        total+=num
    return total

def profileCreation(**kwargs):
    print("User Profile:")
    for key,value in kwargs.items():
        print(f"{key}: {value}")




