# Write your code here

BUY = "buy"
FILL = "fill"
TAKE = "take"
REMAINING = "remaining"
EXIT = "exit"

ACTIONS = (BUY, FILL, TAKE, REMAINING, EXIT)

INGREDIENTS = ("water", "milk", "coffee beans", "disposable cups", )

RECEIPTS = (  # (water, milk, beans, cups), $
    ("espresso", (250, 0, 16, 1), 4),
    ("latte", (350, 75, 20, 1), 7),
    ("cappuccino", (200, 100, 12, 1), 6),
)


def init_limits():
    # [water, milk, beans, cups], money
    return [400, 540, 120, 9], 550


def show_status(supplies, money):
    print()
    print(f"""The coffee machine has:
{supplies[0]} of water
{supplies[1]} of milk
{supplies[2]} of coffee beans
{supplies[3]} of disposable cups
{money} of money\n""")


def ask_action():
    print("Write action ({}):".format(", ".join(ACTIONS)))
    return input()


def ask_coffee_type():
    print("\nWhat do you want to buy? "  # 1 - espresso, 2 - latte, 3 - cappuccino:")
          + ", ".join(["{} - {}".format(x, r[0]) for x, r in enumerate(RECEIPTS, 1)])
          + ", back - to main menu:")
    return input()


def sell_coffee(coffee_type, supplies, money):
    receipt_ingr, receipt_cost = RECEIPTS[coffee_type - 1][1:3]
    new_supplies = []

    for x, y in enumerate(supplies):
        if y >= receipt_ingr[x]:
            new_supplies.append(y - receipt_ingr[x])
        else:
            print(f"Sorry, not enough {INGREDIENTS[x]}!\n")
            return supplies, money
    else:
        print("I have enough resources, making you a coffee!\n")
        return new_supplies, money + receipt_cost


def give_money(money):
    print(f"I gave you ${money}\n")
    return 0


def fill_supplies(supplies):
    print("Write how many ml of water do you want to add:")
    supplies[0] += int(input())

    print("Write how many ml of milk do you want to add:")
    supplies[1] += int(input())

    print("Write how many grams of coffee beans do you want to add:")
    supplies[2] += int(input())

    print("Write how many disposable cups of coffee do you want to add:")
    supplies[3] += int(input())

    print()


limits, balance = init_limits()

#  show_status(limits, balance)

while True:
    action = ask_action()

    if action == BUY:
        coffee_choice = ask_coffee_type()
        if coffee_choice.isnumeric():
            limits, balance = sell_coffee(int(coffee_choice), limits, balance)
        else:
            print()
    elif action == TAKE:
        balance = give_money(balance)
    elif action == FILL:
        fill_supplies(limits)
    elif action == REMAINING:
        show_status(limits, balance)
    elif action == EXIT:
        break
