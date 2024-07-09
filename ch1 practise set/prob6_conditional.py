# Enter four number which is greater  then than print!!!!!
# a1 = int(input("Enter your number 1:"))
# a2 = int(input("Enter your number 2:"))
# a3 = int(input("Enter your number 3:"))
# a4 = int(input("Enter your number 4:"))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("A1 is greater ")

# elif(a2>a1 and a2>a3 and a2>a4):
#     print("A2 is greater ")

# elif(a3>a1 and a3>a2 and a3>a4):
#     print("A3 is greater ")
# elif(a4>a1 and a4>a2 and a4>a3):
#     print("A4 is greater ")

# else:
#     print("Mis match")

# print("End yours Programm!!!!!!!!!!!!!!!!!")


#Q.2  write a program to fnd out whether a student has passed or failed if it requires a totral of 40% and at least 33% in each subject to pass. Assume 3subject and take marks as an input from the  user.

# marks1 = int(input("Enter yours number 1:"))
# marks2 = int(input("Enter yours number 2:"))
# marks3 = int(input("Enter yours number 3:"))

# # check for total percentage

# total_percentage = (marks1+marks2+marks3)/3

# if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
#     print("you are pass",total_percentage)

# else:
#     print(" Fail :) Try again next year",total_percentage)

#Q.3 A spam comment is defined as a text containing followings keywords:
  #   "Make a lot of money", "but now ","subscribe this", "click this ".write a program to detect this these spams.

# p1 = "Make a lot of money"
# p2 = "but now "  
# p3 = "subscribe this"
# p4 = "click this "

# message = input("Enter yours message:")

# if((p1 in message)or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This comment is a spam")

# else:
#     print("This is not a spam")


#Q.4  write a program to find whether a given username contains less than 10 characters or not.


# username = input("Enter username:")

# if(len(username)<10):
#     print("yours username contains less than 10 characters")

# else:
#     print("your username more then or equal to 10 characters!")

# print("End program:)")



#Q.5  write a program which finds out whether a given name is present in a list or not.

# l = ["mithalesh","hemlata","shubham","lavesh","priyanshu"]
# name  = input("Enter yours name:")

# if(name in l):
#     print("Your name is list :",name)
# else:
#     print("mis match , try again")

# print("End programm:)")


#Q.6  write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100=>Ex
#80-90=>A
#70-80=>B
#60-70=>C
#50-60=>D
#<50  =>F

# marks = int(input("enter marks:"))
# if(marks<=100 and marks>=90):
#     grade = "Ex"
# elif(marks<=100 and marks>=90):
#     grade = "Ex"
# elif(marks<90 and marks>=80):
#     grade = "A"
# elif(marks<80 and marks>=70):
#     grade = "B"
# elif(marks<70 and marks>=60):
#     grade = "C"
# elif(marks<60 and marks>=50):
#     grade = "D"
# elif(marks<50):
#     grade = "Fail"

# print("Your grade is:",grade)


#Q.7  write a program to find out whether a given post is talking about "Harry" or not.

post  = input("Enter post:")
if ("Harry".lower() in post.lower()):
    print("This post is talking about harry")

else:
    print("not valid")
