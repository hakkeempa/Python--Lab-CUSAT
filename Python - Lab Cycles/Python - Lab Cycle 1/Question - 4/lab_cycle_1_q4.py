# -*- coding: utf-8 -*-
"""Lab Cycle 1_Q4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iNlm1RqjeyHY-dKHFJVCzHwgQODNhLwv

##**Python - Lab Cylce 1**

**4. Develop a program to perform the following task:
\
a.Define a function to check whether a number is happy or not.
\
b.Define a function to print all happy numbers within a range.
\
c.Define a function to print first N happy numbers.Ahappy numberis a number defined by the following process:
\
•Starting with any positive integer, replace the number withthe sum of the squares of its digits.
\
•Repeat the process until the number equals 1 (where it will stay), or itloops endlessly in a cyclewhich does not include 1.
\
•Those numbers for which this processends in 1are happy.
\
Note: if a number is not being happy after 100 iterations, consider it sad.**
"""

#function - to print happy number's between a range
def print_in_a_range(l,u):
  for i in range(l,u+1):
    #function - check_happy is used to check whether i is a happy number or not
    isHappy = check_happy(i)
    if isHappy:
      print(i,end=",")

#function - to print happy number's upto to a number
def print_upto_n(n):
  for i in range(1,n+1):
    #function - check_happy is used to check whether i is a happy number or not
    isHappy = check_happy(i)
    if isHappy:
      print(i, end=",")


#function - check whether the number is happy or not
def check_happy(num):
  for i in range(0,101):
    happy_sum = 0
    while num>0:
      remainder = num % 10
      num = num //10
      happy_sum = happy_sum + remainder**2
    
    if(happy_sum == 1):
      #returns true if the sum of the squares of its digit is 1
      return True
    else:
      #if the sum is not 1 , then the sum is again passed to the loop
      num = happy_sum
      #after 100 iterations , the number is declared as sad
      if(i == 100):
        return False
      
        
#to - check whether a number is happy or not
num = int(input("Enter the number : "))
result = check_happy(num)
if result:
  print("Happy")
else:
  print("Sad")

#to print happy numbers between a range
lower_range = int(input("Enter the lower limit ")) 
upper_range = int(input("Enter the upper limit ")) 
print_in_a_range(lower_range,upper_range)

#to print happy numbers upto to n value
limit = int(input("\nEnter the numbers upto which you want to print "))
print_upto_n(limit)