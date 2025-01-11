#Banyan Girroir
#Prof Cagney
#CS 161
#1/8/25
#Python - Week 1 HW Assignment
from encodings.punycode import insertion_sort

#part 1
print ('Welcome to my program! ' )
Brother_Sister = "Brother"
Brothers_Name = "Arrow"
print(f"I have a " + Brother_Sister + " and his name is " + Brothers_Name + ".")
print("")

#calculates age, name, and yearly savings
first_name = input("What is your name:")
current_age = int(input("What is your age:"))
yearly_savings = int(input("what is your yearly savings:"))
new_age = current_age+10
five_year_savings = yearly_savings*5
average_monthly_savings = yearly_savings/12
print(f"Hello {first_name}! You are currently {current_age} years old.")
print(f"In 10 years, you will be {new_age} years old.")
print(f"If you save ${yearly_savings} each year, in 5 years you will have saved ${five_year_savings}. ")
print(f"Your average monthly savings is {average_monthly_savings}.")
print("")

#calculates the date and number of days and seconds in the current month
import datetime
import calendar
today = datetime.date.today()
days_in_month = calendar.monthrange(today.year, today.month)[1]
seconds_in_current_month = days_in_month*24*60*60
print("Number of days in the current month:", days_in_month)
print(f"The number of seconds in the current month: {seconds_in_current_month}.")
print("")

#calculates number of dozens and left over eggs
total_eggs = int(input("how many eggs do you have:"))
number_of_dozens = total_eggs//12
number_of_left_over = total_eggs%12
print(f"This makes {number_of_dozens} dozen eggs with {number_of_left_over} left over.")



