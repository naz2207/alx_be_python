#this function is to take a shopping list from the user ,allow edit,remove and display the list
shopping_list = []
def add_item(item):
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")
def  remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")   
def display_list():
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")
