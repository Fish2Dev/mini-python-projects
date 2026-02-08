from sys import exit
todo_list = []
completed_list = []
def add_task():
    user_add_task = input("\nWhat task would you like to add? : ")
    todo_list.append(user_add_task)
    print("\nTask successfully added")
    main()
def view_list():
    print("\nTo-do List:")
    for task in todo_list:
        print(task)
    print("\nCompleted:")
    for comp_task in completed_list:
        print(comp_task)
    user_list_confirm = input("\nType \"DONE\" when done viewing list : ")
    if user_list_confirm == "DONE":
        main()
    else:
        print("That's not a valid input. Please try again")
        view_list()
def mark_task():
    print("\nTo-do List:")
    for task in todo_list:
        print(task)
    print("Completed:")
    for comp_task in completed_list:
        print(comp_task)
    print("")
    user_mark_task = input("Please type out the task you want to mark as completed : ")
    try:
        todo_list.remove(user_mark_task)
        completed_list.append(user_mark_task)
        print("\nUpdated successfully\n")
    except:
        print("Task does not exist. Please try again!")
    main()
def remove_task():
    print("\nTo-do List:")
    for task in todo_list:
        print(task)
    print("Completed:")
    for comp_task in completed_list:
        print(comp_task)
    print("")
    user_remove_task = input("Which task would you like to remove : ")
    try:
        todo_list.remove(user_remove_task)
        print("Updated succesfully")
    except ValueError:
        print("Task does not exist. Please try again!")
    try:
        completed_list.remove(user_remove_task)
    except ValueError:
        pass
    main()
def clear_list():
    todo_list.clear()
    completed_list.clear()
    print("Cleared successfully")
    main()
def main():
    print("\nTo-Do List App\n")
    print("1 - Add Task")
    print("2 - Mark Task As Done")
    print("3 - Remove Task")
    print("4 - View To Do List")
    print("5 - Clear List")
    print("6 - Quit")
    print("")
    user_select = input("Please select a number that corresponds to the function you want to perform: ")
    try:
        int_user_select = int(user_select)
    except ValueError:
        print("\nI'm sorry that is not a vaild option. Please try again.")
    if int_user_select > 6:
        print("\nI'm sorry that is not a vaild option. Please try again.")
    if int_user_select == 1:
        add_task()
    if int_user_select == 2:
        mark_task()
    if int_user_select == 3:
        remove_task()
    if int_user_select == 4:
        view_list()
    if int_user_select == 5:
        clear_list()
    if int_user_select == 6:
        exit()
main()