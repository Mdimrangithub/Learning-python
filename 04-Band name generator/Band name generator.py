#1. Create a greeting for your program.
print("Welcome to the Band name genrater ")
#2. Ask the user for the city that they grew up in.
city = input("Name the city that you grew up?\n")
#3. Ask the user for the name of a pet.
pet_name = input("What is your last pet name?\n")
#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:
sw = city
city = pet_name
pet_name = sw
# Solution: https://replit.com/@appbrewery/band-name-generator-end
print( "Your Band name \n" + city + " " + pet_name )