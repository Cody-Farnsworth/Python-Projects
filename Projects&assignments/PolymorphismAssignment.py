
#parent class
class User:
    name= "Cody"
    email= "cody@gmail.com"
    password= "123456"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and self.entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child Class Empoyee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

    #This is the same method in the parent class
    #The diffrence is that, instead of using password , we're using the pin

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and self.entry_pin == self.pin):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

class Vendor(User):
    vendor_type = "Food"
    vendor_company = "Pepsi"
    vendor_id = "1456_PI"

    #This is the same method in the parent class
    #The diffrence is that, instead of using password , we're using the id.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and self.vendor_id == self.id):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")




if __name__ == "__main__":
    customer = User()
    customer.getLoginInfo()

    manager = Employes()
    manager.getLoginInfo()

    worker = Vendor()
    worker.getLoginInfo()
