def add_to_fruit_bowl():
    return None

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
        ["Lemons", 7]
]
    review_fruit(fruit_list)
    return None

main()