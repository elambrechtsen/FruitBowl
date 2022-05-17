def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string

def review_fruit(l):
    for x in l:
        output = "{:<10} -- {:>4}".format(x[0], x[1])
        print(output)
    return None

def main():
    fruit_list = [
        ["Apple", 2],
        ["Banana", 5],
        ["Pears", 0],
        ["Lemons", 7]]
    menu_list=[
        ["R", "Review fruit"],
        ["Q", "Quit"]
        ]
    run_program=True
    print(menu_list)
    while run_program:
        for x in menu_list:
            output = "{} -- {}".format(x[0], x[1])
            print(output)
        user_choice = get_string("Please select an option: ->").upper()
        print(user_choice)
        if user_choice == "R":
            print(fruit_list)
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry")
    print("Thank you, the program has ended")



if __name__ == "__main__":

    main()

