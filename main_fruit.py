def get_integer(m):
    while True:
        try:
            my_integer = int(input(m))
            return my_integer
        except:
            print("Invalid entry")

def get_string(m):
    my_string = input(m)
    return my_string

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
    #print("Start adding new fruit")
    fruit_name = get_string("Please enter the new fruit: ")
    fruit_number = get_integer("Please enter the number of fruit: ")
    new_list = [fruit_name, fruit_number]
    l.append(new_list)
    #return None

def add_fruit(l):
    print_with_indexes(l)
    user_choice = get_integer("Which option would you like to change: ")
    fruit_name = l[user_choice][0]
    fruit_quantity = l[user_choice][1]
    quantity = get_integer("How many {}s would you like to add ".format(fruit_name))
    l[user_choice][1] += quantity
    print("There has been {} more {}s added to the fruit bowl".format(quantity, fruit_name))

def eat_fruit(l):
    print_with_indexes(l)
    user_choice = get_integer("Which option would you like to change: ")
    fruit_name = l[user_choice][0]
    fruit_quantity = l[user_choice][1]
    quantity = get_integer("How many {} would you like to eat: ".format(fruit_name))
    l[user_choice][1] -= quantity
    print("There has been {} {}s eaten out of the fruit bowl".format(quantity, fruit_name))


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
        ["Q", "Quit"]
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
            run_program == (eat_fruit(fruit_list))
        elif user_choice == "C":
            run_program == (count_fruit(fruit_list))
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry")
    print("Thank you, the program has ended")

if __name__ == "__main__":
    main()
