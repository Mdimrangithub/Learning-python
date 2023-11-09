# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)
year_left = 90 - age_int
month_left = year_left * 12 
day_left = year_left * 360
week_left = year_left * 52

print(f"You have {day_left} days, {week_left} weeks, and {month_left} months left")




