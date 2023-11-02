list_to_do = list()
list_done = list()

def add_item() :
    task  = input("Enter task : ")
    list_to_do.append(task)
    print("Added successfully !")

def print_list_to_do() :
    if len(list_to_do) != 0 :
        i = 1
        for item in list_to_do :
            print("Task ",i," is ",item)
            i+=1
    else :
        print("List To Do is empty !")

def task_done() :
    print_list_to_do()
    if len(list_to_do) != 0 :
        choice = int(input("Enter the number of done task : "))
        if (choice in range(len(list_to_do)+1)) :

            for item in list_to_do :
                if (list_to_do.index(item)+1) == choice :
                    list_done.append(item)
                    list_to_do.remove(item)
                    print("added to done list successfully !")
        else :
            print("Failed choice !")

def print_done_list() :
    if len(list_done) != 0 :
        i=1
        for item in list_done :
            print("Task done ",i," is ",item)
            i+=1
    else :
        print("List of taskes Done is empty !")


while True :
    print(" ")
    print("************ List To Do ***********")

    print("1- Add To Do item.")
    print("2- Print the To Do list.")
    print("3- Move item to done list.")
    print("4- Print the done list.")
    choice = int(input("Enter choice : "))

    if choice == 1 :
        add_item()

    elif choice == 2 :
        print_list_to_do()

    elif choice == 3 :
        task_done()

    elif choice == 4 :
        print_done_list()

    else :
        print("Wrong choice !")
