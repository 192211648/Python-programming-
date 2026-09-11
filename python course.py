# m=int(input("marks in math:"))
# s=int(input("marks in science:"))
# e=int(input("marks in english:"))
# total_marks=m+s+e
# avg_marks=total_marks/3
# percentage=(total_marks/300)*100
# grade=""
# if percentage>90:
#     grade="A"
# elif percentage>80:
#     grade="B"
# elif percentage>70:
#     grade="C"
# elif percentage>60:
#     grade="D"
# else:
#     grade="F"
# print(f"total marks:{total_marks}\navg marks:{avg_marks}\nGrade:{grade}")




# a="radar"
# reverse=a[::-1]
# if reverse==a:
#     print("palindrome")
# else:
#     print("not")

# n=int(input())
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# else:
#     print("zero")



# n=int(input("age:"))
# if n<13:
#     print("Child")
# elif n<=20:
#     print("teenager")
# elif n<=59:
#     print("adult")
# else:
#     print("senior")

# ch=input().lower()
# if ch in "aeiou":
#     print("vowel")
# else:
#     print("consonent")

# n=int(input("num:"))
# if n%3==0 and n%5==0:
#     print("divisable by 3 and 5")
# else:
#     print("not divisable")

# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("sum=",sum)

# n=int(input())
# for i in range(1,11):
#     print(f"{n}X{i}={n*i}")

# n=int(input())
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# n=input()
# print(n[::-1])

# n = int(input())
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# n=int(input())
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)

# a=float(input("num1="))
# b=input("operator:")
# c=float(input("num2="))
# if b=="+":
#     result=a+c
# elif b=="-":
#     result=a-c
# elif b=="*":
#     result=a*c
# elif b=="/":
#     if c==0:
#         result="zero not divide"
#     else:
#         result=a/c
# else:
#     result="invalid operator"
# print(result)

# course="Rakesh is become AIML engineer"
# print(course.title())
# print(course.upper())
# print(course.lower())
# print(course.find("R"))
# print(course.replace("is","will"))
# print("Rakesh" in course)

# a=123
# b=10
# print(a%b)
# print(a//b)
# print(a**b)
# print(type(a/b))
# print(round(a/b))
# print(abs(-156))

# import math
# print(math.ceil(2.1))
# print(math.floor(2.1))
# print(math.factorial(5))
# print(math.copysign(2.1,5))
# print(math.fmod(2.1,4))
# print(math.fabs(2.1))
# print(math.fsum([3.9,2.1]))

# n=input("enter expression:")
# print(int(eval(n)))


# is_hot=False
# if is_hot:
#     print("it is hot")
#     print("drink water")
# else:
#     print("it is cold")
#     print("wear warm clothes")
# print("enjoy day")

# price=100000
# has_good_credit=False
# if has_good_credit:
#     down_payment=0.1*price
# else:
#     down_payment=0.2*price
# print(f"Down payment:${down_payment}")

# has_high_income=True
# has_good_credit=True
# if has_high_income and not has_good_credit:
#     print("eligible for loan")
# else:
#     print("not eligible")

# temp=30
# if temp>30:
#     print("hot")
# elif temp<30:
#     print("cold")
# else:
#     print("it's not hot and cold")

# name=input("enter a name:")
# if len(name)<3:
#     print("name need atleast 3 char")
# elif len(name)<10:
#     print("name is good")
# else:
#     print("name is long")

# w=int(input("weight:"))
# unit=input('(L)bsor(K)g:')
# if unit.upper()=="L":
#     print(f"your {w*0.45} kilos")
# else:
#     print(f"your {w/0.45} lbs")

# i=1
# while i<=5:
#     print('*'*i)
#     i=i+1
# print("done")

# secret_number=9
# guess_limit=3
# guess_count=0
# while guess_count<guess_limit:
#     guess=int(input("guess:"))
#     guess_count+=1
#     if guess==secret_number:
#         print("you guess correct")
#         break
# else:
#     print("sorry you failed")

# command=""

# started=False
# while True:
#     command=input("what:").lower()
#     if command =="start":
#         if started:
#             print("car is already started")
#         else:
#             started=True
#             print("car started")
#             break
#     elif command =="stop":
#         if not started:
#             print("car stopped")
#             break
#     elif command=="help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
# """)
#     elif command=="quit":
#         print("already stop")
# else:
#     print("dont")
# print("tnx")

# prices=[10,20,30]
# total=0
# for price in prices:
#     total+=price
# print(f"total price={total}")

# for i in range(4):
#     for j in range(3):
#         print(i,j)

# n=[5,2,5,2,2]
# for i in n:
#     print("X"*i)

# Google audio problem

# from gtts import gTTS
# text="Hello Diya" 
# tts=gTTS(text=text,lang="en")
# tts.save("hello.mp3")
# print("audio successfully saved")

# name=['john','bob','mosh','sarah','mary']
# print(name[1:])

# n=[3,4,5,6,77,8,9,99,0]
# max=n[0]
# for i in n:
#     if i>max:
#         max=i
# print(max)

# list
# n=[12,1,2,3,4,5,6]
# x=n.count(3)
# print(x)
# n.insert(6,7)
# n.append(10)
# n2=n.copy()
# n.append(11)
# n2.remove(7)
# n2.sort()
# n.sort()
# print(n2)

# n=[12,1,2,23,3,2,2,3]
# unique=[]
# for i in n:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# tuple
# n=(1,2,3)
# x, y, z=n
# print(x*y*z)
# print(n)
# n=(5,1,2,3,4)
# x=n.count(5)
# print(x)

# dictonary

# customer={
#     "name":"rakesh",
#     "age":21,
#     "city":"hyd"
# }
# customer["bithdate"]="april 25 2005"
# print(customer)

# function
# def square(number):
#     return number*number
# result=square(3)
# print(result)

# exception
# try:
#     age=int(input("age:"))
#     income=23456
#     risk=income/age
#     print(risk)
# except ZeroDivisionError:
#     print('age is not be 0')
# except ValueError:
#     print('invalid value')

# class
# class Point:
#     def move (self):
#         print("move")
#     def draw(self):
#         print("draw")

# inheritance
# class Mammal:
#     def walk(self):
#         print("walk")
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
# class Cat(Mammal):
#     def be_annoying(self):
#         print("meow")
# dog1=Dog()
# dog1.bark()

# random values

# import random
# members=['john','mary','bob','mosh']
# leader=random.choice(members)
# print(leader)

# a=6
# Rakesh=7.8
# print(Rakesh+a)
# a,b,c,d=10,20,30,40
# a,b,c,d=d,b,a,c
# print(a,b,c,d)
# print(d,b,a,c)

# y="10+20"
# x=eval('10*x+20*y=0')
# print(x,type(x))
# print(y,type(y))

# formatting
# n=1000000
# print(f"{n:,}")

# name = "Rakesh"
# age = 21
# city = "Tirupati"
# print("Name: {}, Age: {}, City: {}".format(name, age, city))

# name="rakesh"
# print(f"name:{name.title()}")

# n=123412.234567
# print(f"{n:,.2f}")#f is fixed point and .2 is decimal places

# n=0.23456
# print(f"{n:.2%}")

# n=734567
# print(f"{n:0^10}")

name=["rakesh","john","bob","guys"]
age=[29,22,32,21]
course=["CSE","ECE","MECH","AI/ML"]
print(f"{'name':<10}{'age':<10}{'course':<10}")
for i in range (len(name)):
    print(f"{name[i]:<10}{age[i]:<10}{course[i]:<10}")
# for n, a, c in zip(name, age, course):
#     print(f"{n:<10}{a:<10}{c:<10}")

