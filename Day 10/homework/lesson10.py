academy = input("please enter academy in which you study: ")
print (academy)
if academy == "GOA":
    print("good choice")
else:
    print("bad choice")
#homework 2
price = int(input("please enter the price: "))
budget = int(input("please enter your budget:"))
if budget >= price:
    print("you have enough money")
else:
    print("you need",price - budget)
 #homework 3
num1= int(input("please enter your number: "))
if num1 > 5 or num1>= 5:
    print(num1*2)
else:
    print(num1*4)
#homework 4 
ticket_price = 10
ticket_count =int(input("please enter how many ticket you want: "))
if ticket_price <5:
    print("ticket_price * ticket_count")
else:
    discount = ticket_price - ((ticket_price * 30) / 100) 
    print(discount * ticket_count)



#homework 5
num1 = int(input("please enter number 1: "))
num2 = int(input("please enter number 2:"))
operation = input("please enter +,-,* or /: ")
  

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)    
else:
    print("your operation is not valid")