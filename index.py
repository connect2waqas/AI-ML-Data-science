# class Student:
#     name = "waqas khan"


# s1 = Student()

# print(s1)

# print(s1.name)

# s2 = Student()

# print(s2.name)

# class Car:
#     color = "blue"
#     brand = "mercedise"

# car1 = Car()

# print(car1.brand)

# car2 = Car()

# print(car2.color)

# print(car2.brand)

# class Student:
#     def __init__(self,fullname):
#         print(self)
#         self.name = fullname
#         self.roll_no = 92

# s1 = Student("waqas khan")
# print(s1)
# print(s1.name)

# # print(s1.roll_no)

# s2 = Student("yasser khan")

# print(f"this student has name {s1.name} and they have the roll_no of {s1.roll_no}")

    
# class Student:
#     def __init__(self, name , roll_no , marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks


# s1 = Student("waqas",97,972)

# print(s1.name, s1.roll_no , s1.marks)




# print(f"The student that has name {s1.name} of roll no {s1.roll_no} have marks of about {s1.marks}.")

# class Friut:
#     def __init__(self,apple,mango,banana):
#         self.apple = apple
#         self.mango = mango
#         self.banana = banana
    
#     def welcome(self):
#         print("Hello welcome")
    
#     def marks(self):
#         return self.mark


# friut1 = Friut(1000,2000,4000)

# print(f"i have about total apple{friut1.apple} banana{friut1.banana} mango{friut1.mango}")

# friut1.welcome()

# print(friut1.apple,friut1.banana,friut1.mango)

# class Student:
#     def __init__(self, name ,marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         for val in self.marks:
#             sum = 0
#             sum +=val
#         print(f"hi {s1.name} your avg_score is:", sum / 3)





# s1 = Student("waqas khan",[45,32,99])

# print(s1.get_avg())

# class Student:
#     def __init__(self,name,age, semes , college):
#         self.name = name
#         self.age = age
#         self.semes = semes
#         self.college = college
    
#     def get_student_info(self):
#         return f"i am {self.name} . my age is {self.age} . my current semester is {self.semes} in the  of {self.college}"
    

# s1 = Student("waqas khan", 19 , "1st" , "university of haripur.")

# s2 = Student("roman khan",20,"no semeseter","no college")

# print(s1.get_student_info())


# class Student:
#     def __init__(self,name,subject,marks):
#         self.name = name
#         self.subject = subject 
#         self.marks = marks
    
#     def avg_score(self):
#         sum  = 0
#         for val in self.marks:

#             sum +=val

#             return f"Hi {self.name} your avg_score of {self.marks} is about is : {sum/3}"
    

# s1 = Student("waqas ","artificial intelligence",[98,34,23])
# s1.avg_score()
# print(s1.avg_score())


# class Area:
#     def __init__(self, side1):
#         self.side1 = side1
#     def total_area(self):
#         area = self.side1 * self.side1
#         return area
    
# Area1 = Area(5)
# print(Area1.total_area())


# class Area_of_cirle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area_of_circle(self):
#         area_of_circle = 3.14 * (self.radius*self.radius)

#         return area_of_circle

# area_of_circle1 = Area_of_cirle(2)

# print(area_of_circle1.area_of_circle())


# class Account:
#     def __init__(self,balance,acc_no):
#         self.balance = balance
#         self.acc_no = acc_no

#     def debat(self , amount):
#         self.balance -= amount
#         print("Rs.", amount , "was debated from your account")
#         print("Total balance is :",self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount , "was credited from your account")
#         print("Total balance is :",self.get_balance())

    
#     def get_balance(self):
#         return self.balance
        



# # acc1 = Account(10000,21034)

# acc1.debat(1000)
# acc1.credit(500)
        


# class Account:
#     def __init__(self,pen , acc):
#         self.pension = pen
#         self.acc = acc

    
#     def debat(self,amount):
#         self.pension -= amount
#         print(f"Rs.", amount , "has been debated :")
#         print(self.pension)
    

#     def credit(self,amount):
#         self.pension += amount
#         print(f"Rs.", amount , "has been credited:")
#         return self.pension

#     def pension(self):
#         return self.pension



# acc1 = Account(10000, 9721)

# print(acc1.credit(500))

# print(acc1.pension)


# class Store():
#     def __init__(self,books,cloths ,account = 0):
#         self.books = books
#         self.cloths = cloths
#         self.account = account
    
#     def sell_books(self,sel,Rs):
#         self.books -= sel 
#         earning = sel*Rs
#         self.account +=earning
#         return self.books

    
#     def sell_clothes(self,sel,Rs):
#         self.cloths -= sel
#         earning = sel*Rs
#         self.account += earning
#         return self.cloths


# store_selling = Store(500,10)

# print(store_selling.sell_books(100,2))

# print(f"Updated account balance: {store_selling.account} Rs")  # This will print the updated account balance


#  we have to make an account for the store . By each from the store we have to uptade the account and make it proper usable.


# class Store:
#      def __init__(self,iphone,andriod,Handfree,account = 0): # This is constructor mean after we have a blueprint
#         self.account = account
#         self.iphone = iphone
#         self.andriod = andriod
#         self.Handfree = Handfree
    
#      def sell_iphone(self,sel,Rs = 200):
#         self.iphone -= sel
#         earning = sel*Rs
#         self.account +=earning
#         print(f"earning is equal to ::{self.account} and other is :: {self.iphone}")
    
#      def sell_anodriod(self,sel,Rs = 20):
#         self.andriod -= sel
#         earning = sel * Rs
#         self.account += earning
#         return f"{self.account} and {earning}"
    
#      def account_balance(self):
#         return self.account



# first_sell = Store(500,300,200)

# print(first_sell.sell_iphone(20))

# print(first_sell.sell_anodriod(2))


# print(first_sell.account_balance())


#  SO HERE WE TOWORD THE NEW TOPIC AND MAKE ANOTHER CONCEPT BRIGHT AND CLEAR .

#  it is inheritance and polymorphism

# class Student:
#     def __init__(self,name , roll_no):
#         self.name = name
#         self.roll_no = roll_no

# s1 = Student("Roman khan", 48)

# print(s1.name)
# del s1.name 
# print(s1.name) it show error  becuase we have delete the student name

# class Car:
#     @staticmethod
#     def start():
#         return f"Car Started.."
    
#     @staticmethod
#     def stop():
#         return f"Car stopped.."

# class Toyota(Car):
#     def __init__(self , name):
#         self.name = name


# car1 = Toyota("furtuner")

# print(car1.start())

# print(car1.stop())

# class Car:
#     colour = "black"
#     price = 100000
#     speed = "200 kilometer"
#     @staticmethod
#     def start():
#         return f"Car started..."
    
#     @staticmethod
#     def stop():
#         return f"Car stopped.."
# class Toyata(Car):
#     def __init__(self,name, engine):
#         self.name = name
#         self.engine = engine
    
# car1 = Toyata("mercedise","125 icc")

# car2 = Toyata("furtuner", "450 icc")

# print(car1.start())

# print(car2.name)

# print(f"The car {car2.name} has {Car.colour} colur  and in the speed of {Car.speed} and it will started when i call the function..{car1.start()}")


#  after we have to discuse its types that is very essential for everyone to know..

# class Father:
    # colour = "white"
    # height = "6 feet"
#     weight = "60kg"
#     eye_colour = "blue"
#     age = 47

# class Mother:
#     colour = "black"
#     height = "5"
#     weight = "45kg"
#     eye_colour = "blackish"
#     age = 37

# class Son(Father,Mother):
#     def __init__(self,name):
#         self.name = name
#         # self.age = age



# son1 =Son("Tony stark")

# print(f"The father son named {son1.name} has age difference of {Father.age - Mother.age}. \n"
#       f"He has eye colour of {Mother.eye_colour}. His weight is {(int(Mother.height))**2}.")
 

#  So let start we have to create a calculator. using our potential of coding


# num1 = int(input("Enter a number to perform an operation :: "))

# operator = input("enter an operator ::")

# num2 =int(input("Enter any other number :: "))

# if operator == "+" :
#     sum_result = num1 + num2
#     print("sum = ",sum_result)
# elif operator == "-":
#     difference = num1 - num2
#     print("difference = ",difference)
# elif operator == "*":
#     multiplication = num1 * num2
#     print("multiplication = ",int(multiplication))

# elif operator == "/":
#     if num2 == 0 or num2 == 0:
#         divsion = 0
#         print("division =",divsion)
#     else:
#         divsion = num1 / num2 or num2 / num1
#         print("division =",divsion)

# else:
#     print("enter right one!")

#  after that we have to create a calender through the python code so let start::



# num = int(input("enter a number  for a month :: "))

# if num == 1:

#     print("JANUARY")

# elif num == 2:

#     print("FEBRUARY")

# elif num == 3:

#     print("MARCH")

# elif num == 4:

#     print("APRIL")

# elif num == 5:

#     print("MAY")

# elif num == 6:

#     print("JUN")

# elif num == 7:

#     print("JULY")

# elif num == 8:

#     print("AUGUST")

# elif num == 9:

#     print("SEPTEMBER")

# elif num == 10:

#     print("OCTOBER")

# elif num == 11:

#     print("NOVEMBER")

# elif num == 12:

#     print("DECEMBER")

# else:
#     print("invalid integer!")

# class Car:
#     @staticmethod
#     def star():
#         print("car started...")
    
#     @staticmethod
#     def stop():
#         print("car stopped..")

# class ToyataCar(Car):
#     def __init__(self,brand,colur):
#         self.brand = brand
#         self.colur = colur

# class Forturner(ToyataCar):
#     def _init__(self,type,glass):
#         self.type = type
#         self.glass = glass


# car1 = Forturner("electric","bullout proof")
# print(car1.star())

# class A:

#     varA= f"Welcome to class A"

# class B:

#     varB= f"Welcome to class B"

# class C:

#     varC= f"Welcome to class C"

# class Child(A,B,C):

#     f"Welcome to child class"

# c1 = Child()

# print(c1.varA)

# print(c1.varB)

# print(c1.varC)

# average = lambda x , y : (x + y) / 2

# print("average is ",average(5,10))


# addition = lambda x , y : x + y 

# print("number addition is ",addition(100,200))

