'''
Inputs
-age
-day of week
-height
-vip
-Signed waiver
-Partent present

Processes:

-Use the variables to identify when rides are available

Outputs:
-A list of rides


'''


age = int(input("Age: "))
day_of_week = input("What day is it?: ").lower()
height = int(input("Please enter your height in inches: "))
vip = input("VIP? (yes or no): ").lower()
signed_waiver = input("Signed waiver? (yes or no): ").lower()
parent_present = input("Parent present?(yes or no): ").lower()

#Megadrop

# if age >= 14 and signed_waiver == "yes" and (height >= 54 or (height >=50 and vip == "yes")):
#     print("Megadrop")

ride_found = False

if age >= 14 and signed_waiver == "yes":
    if height >=54:
        print("Megadrop")
        ride_found = True
    elif height >= 50 and vip == "yes":
        print("Megadrop")
        ride_found = True

if age >= 10 and height >= 48 and day_of_week != "monday":
    print("Thunderbolt")
    ride_found = True

if age > 8 or parent_present == "yes":
    print("Kiddie Coaster")
    ride_found = True

if ride_found == False:
    print("No rides available")