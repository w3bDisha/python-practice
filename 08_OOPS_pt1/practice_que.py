# Q.Create a student c;ass that takes name and
#marks of 3 subjects as argument in constructor
#then create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name,"your avg score is :",sum/3)

s1 = Student("Tony stark", [99, 98, 88])
s1.get_avg()

s2 = Student("Ellie", [96, 98, 87])
s2.get_avg()

s3 = Student("Goldie", [90, 78, 91])
s3.get_avg()

print("\n")

#Create Account class with 2 attributes - balance and account no.
#create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance
    

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)



