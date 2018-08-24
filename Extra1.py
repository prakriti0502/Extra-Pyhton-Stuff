#1. accepts the gender in terms of male or female from user. (if client enters wrong input instead of putting error it will display an appropriate msg And exits. )
gender = input("Enter gender\t")
if gender == 'male' or gender == 'female'or gender == 'Male' or gender == 'Female' or gender == 'MALE' or gender == 'FEMALE':
    print("Correct")
else:
    print("wrong input")

#2. Accept the name, and prints the name with salutation according to gender like sir  ( "Hello input-wala-name, sir") for male and mam for female...
name = input("Enter name ")
gen = input("Enter sex, m for mae, f for female ")
if name.isalpha():
    if gen == 'm':
        print("Hello {} sir".format(name))
    elif gen == 'f':
        print("Hello {} ma'am".format(name))
    else:
        print("Wrong gender entered, enter only m or f")
else:
    print("Wrong name entered")


'''3. Ask their age and check the age criteria, if the age of man is greater than 20, it  will print.. you are  able  to enroll
    for python fundamental course otherwise it will display an msg that you are below age criteria
    you can't enroll the course..and exits. (program does not throw any kind of error here.) '''
age = int(input("Enter age "))
if age>20:
    print("You are able to enroll for python fundamental course")
else:
    print("you are below age criteria and you can't enroll the course..")


#4.if Age of women is greater than 19 she is available to enroll for core Java course.(same criteria error will not displayed)
age = int(input("Enter age "))
if age>19:
    print("You are able to enroll for java course")
else:
    print("you are below age criteria and you can't enroll the course..")


'''5. If user enters wrong value like in case of input of name of he enters numeric value, does not enter name by passing simply enter,
    it will guide the user to enter alphabetic value and some text incase of blank input. '''

name = input("Enter name ")
age = input("Enter age ")
if name.isalpha():
    print("Name is ",name)
else:
    print("Wrong input, enter alphabetical name")
if age.isnumeric():
    print("Age is ",age)
else:
    print("Enter ony numeral age")



