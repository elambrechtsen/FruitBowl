def get_integer(m):
    while True:
        try:
            my_integer = int(input(m))
            return my_integer
        except:
            print("Invalid entry, re-read the question")

def get_string(m):
    my_string = input(m)
    return my_string

def get_integer_limits(m, a, b):
    while True:
        try:
            my_integer = int(input(m))
        except:
            print("Invalid entry")
            continue
        if my_integer < a or my_integer > b:
            print("Not in correct range")
        else:
            return my_integer

def review_fruit(l):
    for x in l:
        output = "{:<10} -- {:>4}".format(x[0], x[1])
        print(output)
    return None

def print_with_indexes(l):
    for i in range (0, len(l)):
        output = " {:3} : {:10} {:10}".format(i, l[i][0], l[i][1])
        print(output)

def add_new_entry(l):
    fruit_name = get_string("Please enter the new fruit: ").title()
    for x in l:
        if fruit_name == x[0]:
            output = "This fruit is already in the list please add to the existing amount"
            print(output)
            return None
    fruit_number = get_integer("Please enter the number of fruit: ")
    new_list = [fruit_name, fruit_number]
    l.append(new_list)
    return None

def add_fruit(l):
    print_with_indexes(l)
    user_choice = get_integer("Which option would you like to change: ")
    fruit_name = l[user_choice][0]
    fruit_quantity = l[user_choice][1]
    quantity = get_integer("How many {}s would you like to add ".format(fruit_name))
    l[user_choice][1] += quantity
    print("There has been {} more {}s added to the fruit bowl".format(quantity, fruit_name))


def remove_fruit(L):
    print_with_indexes(L)
    my_index = get_integer("Choose index number to update the fruit quantity")
    print()
    old_amount = L[my_index][1]
    number = get_integer_limits("Enter how many you would like to remove:", 0, old_amount)
    print()
    new_amount = old_amount - number
    print("{} - {} = {} left in the bowl".format(old_amount, number, new_amount))
    print()
    output_message = "The number of {} {} has been updated to {}.".format(old_amount, L[my_index][0], new_amount)
    print(output_message)

#def eat_fruit(l):
    #print_with_indexes(l)
    #user_choice = get_integer("Which option would you like to change: ")
    #fruit_name = l[user_choice][0]
    #fruit_quantity = l[user_choice][1]
    #old_amount = l[0]
    #quantity = get_integer_limits("How many {} would you like to eat: ", 0, old_amount.format(fruit_name))
    #l[user_choice][1] -= quantity
    #print("There has been {} {}s eaten out of the fruit bowl",.format(quantity, fruit_name))


def update_fruit(l):
    print_with_indexes (l)
    user_choice = get_integer("PLease enter the index number to update the name: ")
    #print(L[my_index])
    new_fruit = get_integer("Please enter the new quantity of fruit: ")
    old_fruit = l[user_choice][1]
    l[user_choice][1] = new_fruit
    #print(l [my_index][1])
    output_message = "{} many has now been changed to {}".format(old_fruit, new_fruit)
    print(output_message)

def count_fruit(l):
    total = 0
    for x in l:
        total += x[1]
    print(total)

def main():
    fruit_list = [
        ["Apple", 2],
        ["Banana", 5],
        ["Pear", 0],
        ["Lemon", 7]]
    menu_list = [
        ["R", "Review fruit"],
        ["N", "New type of fruit"],
        ["Q", "Change quantity of fruit"],
        ["A", "Add more fruit"],
        ["E", "Eat fruit"],
        ["C", "Count fruit in bowl"],
        ["S", "Stop program"]
        ]
    #add_new_entry(fruit_list)

    run_program=True
    while run_program:
        for x in menu_list:
            output = "{} -- {} ".format(x[0], x[1])
            print(output)
        user_choice = get_string("Please select an option: ->").upper()
        print(user_choice)
        if user_choice == "R":
            print(fruit_list)
        elif user_choice == "N":
            run_program ==(add_new_entry(fruit_list))
        elif user_choice == "Q":
            run_program ==(update_fruit(fruit_list))
        elif user_choice == "A":
            run_program ==(add_fruit(fruit_list))
        elif user_choice == "E":
            run_program == (remove_fruit(fruit_list))
        elif user_choice == "C":
            run_program == (count_fruit(fruit_list))
        elif user_choice == "S":
            run_program = False
        else:
            print("Unrecognised entry")
    print("Thank you, the program has ended")

if __name__ == "__main__":
    main()
