import menu_actions

loop = True

while loop:  # While loop keeps going until loop false
    menu_actions.print_menu()  # Display Menu
    choice = int(input("Select an action: "))

    if choice == 1:
        menu_actions.action_one()
    elif choice == 2:
        menu_actions.action_two()
    elif choice == 3:
        loop = False  # Ends while loop
    else:
        input("Invalid choice.")  # Invalid input gives error message

