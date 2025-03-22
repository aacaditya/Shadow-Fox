# 1. Write a program to determine the BMI Category based on user input. 
#    Ask the user to: 
#    Enter height in meters 
#    Enter weight in kilograms 
#    Calculate BMI using the formula: BMI = weight / (height)2 
#    Use the following categories: 
#    If BMI is 30 or greater, print "Obesity" 
#    If BMI is between 25 and 29, print "Overweight" 
#    If BMI is between 18.5 and 25, print "Normal" 
#    If BMI is less than 18.5, print "Underweight" 
#    Example: 
#    Enter height in meters: 1.75 
#    Enter weight in kilograms: 70 
#    Output: "Normal" 

height=float(input("enter the height:"))
weight=float (input("enter the weight:"))
BMI=weight/(height*height)
if BMI >=30:
    category="obesity"

elif 25 <= BMI < 29 :
    category="Overweight"

elif 18.5 <= BMI < 25 :
    category="Normal"


else :
    category="Underweight"

print(f"BMI category is: {category}")


#  2. Write a program to determine which country a city belongs to. Given
#     list of cities per country: 
#     Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"] 
#     UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
#     India = ["Mumbai", "Bangalore", "Chennai", "Delhi"] 
#     Ask the user to enter a city name and print the corresponding country.
#     Example: 
#     Enter a city name: "Abu Dhabi" 
#     Output: "Abu Dhabi is in UAE"
  
countries={
    "Australia":["Sydney","Melbourne","Brisbane","Perth"],
    "UAE":["Dubai","Abu Dhabi","Sharjah","Perth"],
    "India":["Mumbai","Bangalore","Chennai","Delhi"]
}

city=input("Enter the city name :")
found = False
for country,cities in countries.items():
    if city in cities:
        print(f"{city} is in {country}.")
        found=True
        break

if not found:
    print("city is not found in the list:")

# If Condition (Continued...)
# 3. Write a program to check if two cities belong to the same country.
#    Ask the user to enter two cities and print whether they belong to the
#    same country or not. 
#    Example: 
#    Enter the first city: "Mumbai" 
#    Enter the second city: "Chennai" 
#    Output: "Both cities are in India" 
#    Example: 
#    Enter the first city: "Sydney" 
#    Enter the second city: "Dubai" 
#    Output: "They don't belong to the same country" 
countries={
    "Australia":["Sydney","Melbourne","Brisbane","Perth"],
    "UAE":["Dubai","Abu Dhabi","Sharjah","Perth"],
    "India":["Mumbai","Bangalore","Chennai","Delhi"]
}
city1=input("Enter the first city:")
city2=input("Enter the second city:")

country1 = None
country2 = None
for country,cities in countries.items():
    if city1 in cities:
        country1=country
    if city2 in cities:
        country2=country

if country1 and country2:
    if country1 == country2:
        print("f Both cities are in {country1}")
    else:
        print("They don't belong to same country")
else:
    print("One or both cities are not in the list")
