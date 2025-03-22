# 1. Write a function that takes two arguments, 145 and 'o', and uses the 'format' function to return a formatted string. Print the result. Try to identify the representation used.

def format_number(number,representation):
    return format(number,representation)

result = format(145,'o')
print(result)

# 2. In a village, there is a circular pond with a radius of 84 meters.
#    Calculate the area of the pond using the formula: Circle Area = π
#    r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
#    1.4 liters of water in a square meter, what is the total amount of
#    water in the pond? Print the answer without any decimal point in
#    it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
#    Water per Square Meter

R=84
A=3.142*R*R
W=1.4

T=W * A 
print("Total:",T)

# 3. If you cross a 490 meterlong street in 7 minutes, calculate your
#    speed in meters per second. Print the answer without any decimal
#    point in it. Hint: Speed = Distance / Time 

D = 490
T = 7

S = D/T

print("Speed in meter :",int(S))


