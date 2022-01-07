

from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
    #this function is telling us to pass in an argument, but we wont tell you how or what
    #kind of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(car):
#here we've defined how to implemnt the payment function from its parent payslip class.
    def payment(self, amount):
        print("Your purchase amount of {} exceeded you $100 limit ".format(amount))



if __name__ == "__main__":
    obj = DebitCardPayment()
    obj.paySlip("$400")
    obj.payment("$400")
    
