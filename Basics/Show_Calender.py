#This python code displays calender of any month in any year
import calendar     #Calender library has been used to get the calender

yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
#The following code displays calender of entered month and year
# display the calendar
print("Here you go.......")
print(calendar.month(yy,mm))  
