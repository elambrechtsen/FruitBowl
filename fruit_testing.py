def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string

def add_to_fruit_bowl():
    return None

def review_fruit(l):
    for x in l:
        output = "{:<10} -- {:>4}".format(x[0], x[1])
        print(output)
    return None

def print_with_indexes(l):
    for i in range (0, len(l)):
        output = " {} : {} ".format(i, l[i][0], l[i][1])
        print(output)

def add_new_entry(l):
    print("Start adding new fruit")
    fruit_name = get_string("Please enter the new fruit: ")
    fruit_number = get_string("Please enter the number of fruit: ")
    new_list = [fruit_name, fruit_number]
    l.append(new_list)
    return None

def main():
    fruit_list = [
        ["Apple", 2],
        ["Banana", 5],
        ["Pears", 0],
        ["Lemons", 7]]
    #review_fruit(fruit_list)
    #return None

    add_new_entry(fruit_list)
    print_with_indexes(fruit_list)

main()

