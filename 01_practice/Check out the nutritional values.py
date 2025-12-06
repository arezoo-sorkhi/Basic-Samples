#Check out the nutritional values of an Oreo cookie. Koppelingen naar een externe site.

#Write code that does the following: 

#calculate how much one Oreo cookie is concerning: calories, sodium, carbohydrate, fat 
#create a user input that asks how much cookies you ate 
#calculate how much calories, etc. you consumed 
#warn the user that if he/she surpasses 2000kcal he/she should stop eating these darn delicious cookies 
#use variables! 
#save the file as assignment01yourlastname.py



# calculate how much one Oreo cookie is concerning: calories, sodium, carbohydrate, fat
# 3 cookies
calories_3_cookies = 160       # kcal
carbs_3_cookies = 25            # g
fat_3_cookies = 7.0             # g 
sodium_3_cookies = 160          # mg

# 1 cookies
calories_per_cookie = calories_3_cookies / 3
carbs_per_cookie = carbs_3_cookies / 3
fat_per_cookie = fat_3_cookies / 3
sodium_per_cookie = sodium_3_cookies / 3


#create a user input that asks how much cookies you ate 
num_cookies = int(input("How many Oreo cookies did you eat? "))


#calculate how much calories, etc. you consumed 
total_calories = num_cookies * calories_per_cookie
total_carbs = num_cookies * carbs_per_cookie
total_fat = num_cookies * fat_per_cookie
total_sodium = num_cookies * sodium_per_cookie


# Results
print("You ate", num_cookies, "Oreo(s)")
print("Total calories:", total_calories, "kcal")
print("Total carbohydrate:", total_carbs, "g")
print("Total fat:", total_fat, "g")
print("Total sodium:", total_sodium, "mg")


#warn the user that if he/she surpasses 2000kcal he/she should stop eating these darn delicious cookies 
if total_calories > 2000:
    print("Warning: You have surpassed 2000 kcal — maybe stop eating these darn delicious cookies!")