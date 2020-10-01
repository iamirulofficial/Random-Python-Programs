#Finding the missing digits in a phone number
nu=input("Enter your phone number:")
l=list(nu)
if len(l)==10 and nu.isnumeric():      #checking whether the entered is a phonenumber or not
    for i in range(10):
        if str(i) not in l:
            print(str(i)+" is not in your phone number")
else:
    print("There should be 10 digits in phone number and it should not contain alphabets")
