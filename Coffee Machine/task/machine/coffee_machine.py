# Write your code here

BUY = "buy"
FILL = "fill"
TAKE = "take"

ACTIONS = (BUY, FILL, TAKE)

RECEIPTS = (  # (water, milk, beans, cups), $
    ("espresso", (250, 0, 16, 1), 4),
    ("latte", (350, 75, 20, 1), 7),
    ("cappuccino", (200, 100, 12, 1), 6),
)


def init_limits():
    # [water, milk, beans, cups], money
    return [400, 540, 120, 9], 550


def show_status(supplies, money):
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
    print("What do you want to buy? "  # 1 - espresso, 2 - latte, 3 - cappuccino:")
          + ", ".join(["{} - {}".format(x, r[0]) for x, r in enumerate(RECEIPTS, 1)]) + ":")
    return int(input())


def sell_coffee(coffee_type, supplies):
    receipt_ingr, receipt_cost = RECEIPTS[coffee_type - 1][1:3]
    for x, y in enumerate(supplies):
        #    supplies = [x - y for x, y in zip(supplies, receipt_ingr)]
        supplies[x] = y - receipt_ingr[x]
    return receipt_cost


def give_money(money):
    print(f"I gave you ${money}")
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


limits, balance = init_limits()

show_status(limits, balance)
action = ask_action()

if action == BUY:
    coffee_choice = ask_coffee_type()
    balance += sell_coffee(coffee_choice, limits)
elif action == TAKE:
    balance = give_money(balance)
elif action == FILL:
    fill_supplies(limits)

print()
show_status(limits, balance)
