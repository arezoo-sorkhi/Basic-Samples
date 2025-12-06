# Exercise 3: Simple login system 

# Create a static dictionary with a number of users and with the following values: 
# 1.First name
# 2.Last name
# 3.Email address
# 4.Password
# Ask the user for: 
# 5.Email address
# 6.Password
#Loop (for()) through the dictionary and if (if()) the user is found print the following: 
#7. Hello, first name last name you have successfully logged in
#8. Notify the user if the password and email address are wrong
#9. Additional challenge: if you want the program to keep asking for a username and password when the combination is wrong, you will need a while() loop.
#10. Save the file as assignment03yourlastname.py 



# Create a static dictionary with a number of users and with the following values: 
users = {
    1: {"first_name": "Ali", "last_name": "Sorkhi", "email": "ali@example.com", "password": "1234"},
    2: {"first_name": "Sara", "last_name": "Moradi", "email": "sara@example.com", "password": "abcd"},
    3: {"first_name": "John", "last_name": "Doe", "email": "john@example.com", "password": "pass"}
}



# Ask the user for: 
# 5.Email address
# 6.Password
#Loop (for()) through the dictionary and if (if()) the user is found print the following: 
#7. Hello, first name last name you have successfully logged in
#8. Notify the user if the password and email address are wrong
#9. Additional challenge: if you want the program to keep asking for a username and password when the combination is wrong, you will need a while() loop.
while True:
    # Get email and password from user
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")

    login_success = False

    # Loop through users
    for user in users.values():
        if user["email"] == email_input and user["password"] == password_input:
            print("Hello,", user["first_name"], user["last_name"], "you have successfully logged in!")
            login_success = True
            break

    if login_success:
        break
    else:
        print("Email or password is wrong. Please try again.\n")