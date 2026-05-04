'''
Inputs:
- weight in pounds
- height in inches
- name
-age
-sex


Processes:
- Checks if the input is a valid number
- If the input is valid, it calculates the BMI using the formula: BMI = weight / (height)^2 *703
- Categorizes BMI
    -underweight <18.5
    -healthy 18.5-24.9
    -overweight 25-29.9
    -obesity 30-39.9
    -severe obesity >40 


Outputs:

- The report for the individual



'''

#collect inputs
name = input("Please enter your name: ")
weight = input("Please enter your weight in pounds: ")
height = input("Please enter your height in inches: ")
age = input("Please enter your age: ")
sex = input("What is your sex?: ").lower()

# validate inputs

age = age.replace(".", " ", 1)
age_is_int = age.isdigit()
if age_is_int == True:
    age = int(age)
age_is_reasonable = True
if age_is_int == True and (age < 140 or age > 1):
    age_is_reasonable = True


sex_is_valid = False
if sex == "male" or sex == "female":
    sex_is_valid = True

height = height.replace(".", " ", 1)
height_is_int = height.isdigit()
if height_is_int == True:
    height = int(height)
height_is_reasonable = False
if height_is_int == True and (height >= 12 or height <= 140):
    height_is_reasonable = True

weight = weight.replace(".", " ", 1)
weight_is_int = weight.isdigit()
if weight_is_int == True:
    weight = int(weight)
weight_is_reasonable = False
if weight_is_int == True and (weight >= 12 or weight <= 1200):
    weight_is_reasonable = True

ready_to_process = True

if age_is_int == False or age_is_reasonable == False:
    print("You entered a non-expected age, plase use whole numbers.")
    ready_to_process = False

if sex_is_valid == False:
    print("You entered a non-expected sex. Please use male or female.")
    ready_to_process = False

if height_is_int == False or height_is_reasonable == False:
    print("You entered a non-expected height, please use whole numbers.")
    ready_to_process = False

if weight_is_int == False or weight_is_reasonable == False:
    print("You entered a non-expected weight, please use whole numbers.")
    ready_to_process = False


if ready_to_process == True:
    bmi = weight / (height ** 2) * 703
    bmi_category = ""
    if bmi < 18.5:
        bmi_category = "underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        bmi_category = "healthy"
    elif bmi >= 25 and bmi <= 29.9:
        bmi_category = "overweight"
    elif bmi >= 30 and bmi <= 39.9:
        bmi_category = "obese"
    elif bmi > 40:
        bmi_category = "severely obese"

#Report
        
    print(f"Report for {name}:\n"
      f"{age} year old {sex}\n"
      f"Your Bmi is {bmi:.2f}, which is considered {bmi_category}.")