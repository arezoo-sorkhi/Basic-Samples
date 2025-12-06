# Simple to-do list program

# Create a simple to-do list using a list. 
# Make sure the code contains the following actions as listed below 
# (this can be sequential i.e. in steps so no need to overthink it): 
# add a task to the to-do list with append() 
# add a task to the to-do list with append() 
# add a task to the to-do list with append() 
# add a task to the to-do list with an input() 
# print the number of tasks in the to-do list 
# remove the first task of the to-do list 
# remove a specific task of the to-do list 
# tell the user that if he/she has less than 4 tasks on the to-do list she has time to do more 
# tell the user that if he/she has more or equal than 6 items she has no room to do more tasks 
# save the file as assignment02yourlastname.py 



# Create a simple to-do list using a list
todo_list = ["Study","Cleaning"]


# add a task to the to-do list with append() 
todo_list.append("Edit Video")


# add a task to the to-do list with an input() 
task_Input = input("Enter a new task: ") 
todo_list.append(task_Input)


# print the number of tasks in the to-do list 
print("Number of tasks:", len(todo_list))


# remove the first task of the to-do list 
todo_list.pop(0)


# remove a specific task of the to-do list 
specific_task_remove =input("Enter a task you want to remove: ")
if specific_task_remove in todo_list:
    todo_list.remove(specific_task_remove)
    print("Removed:", specific_task_remove)
else:
    print("Task not found:", specific_task_remove)


# tell the user that if he/she has less than 4 tasks on the to-do list she has time to do more
if len(todo_list) < 4:
    print("You have time to do more tasks.")



# tell the user that if he/she has more or equal than 6 items she has no room to do more tasks 
if len(todo_list) >= 6:
    print("You have no room to do more tasks.")

# Print final list
print("Final to-do list:", todo_list)