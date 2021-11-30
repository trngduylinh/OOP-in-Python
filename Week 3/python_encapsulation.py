#Encapsulation

class info:

    public = "pub"  
    _protected = "pro"    
    __private = "priv"

    print(__private)

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def __name(self):
        print("Name : ", self.firstname, self.lastname)
    
    def age(self, age):
        print("Age : ", age)

class Encap(info):
    pass



print(info.public)
info.__name()

s1 = Encap("A", "B")
print(s1._protected)
print(s1.__private)







