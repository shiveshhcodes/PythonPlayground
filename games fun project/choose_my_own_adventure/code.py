name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

print("You stand at a village crossroads. To your left, a bustling marketplace. To your right, a misty path to ancient ruins.")

choice = input("Which direction do you choose? (left/right) ")

if choice == "left":
    print("In the marketplace, a merchant offers you a wish-granting amulet. Do you accept (accept) or decline (decline)?")

    market_choice = input()

    if market_choice == "accept":
        print("You accept the amulet and find yourself in a palace. A being offers to fulfill your wish. Do you wish (wish) or return the amulet (return)?")

        palace_choice = input()

        if palace_choice == "wish":
            print("Your wish is granted, but with a hidden cost. Your life is forever changed.")
        elif palace_choice == "return":
            print("You return the amulet, realizing happiness lies in the journey. The merchant rewards you with a treasure.")
        else:
            print("Invalid choice! The amulet's magic dissipates.")

    elif market_choice == "decline":
        print("You decline the amulet. The merchant gives you bread. You see a lost child. Do you help (help) or continue (continue)?")

        help_choice = input()
else:
    print("You chose the misty path and venture into the unknown.")
