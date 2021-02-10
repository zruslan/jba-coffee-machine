# Write your code here
class CoffeeMachine:
    BUY = "buy"
    FILL = "fill"
    TAKE = "take"
    REMAINING = "remaining"
    EXIT = "exit"

    ACTIONS = (BUY, FILL, TAKE, REMAINING, EXIT)

    INGREDIENTS = ("water", "milk", "coffee beans", "disposable cups",)
    ING_QUESTIONS = ("Write how many ml of water do you want to add:",
                     "Write how many ml of milk do you want to add:",
                     "Write how many grams of coffee beans do you want to add:",
                     "Write how many disposable cups of coffee do you want to add:",
                     )

    RECEIPTS = (  # (water, milk, beans, cups), $
        ("espresso", (250, 0, 16, 1), 4),
        ("latte", (350, 75, 20, 1), 7),
        ("cappuccino", (200, 100, 12, 1), 6),
    )

    # 3 kinds of expecting user input - 3 major states
    CHOOSE_ACTION = 1
    CHOOSE_COFFEE = 2
    FILL_SUPPLIES = 3
    EXITING = 4  # Technical final state for exit

    def __init__(self):
        self.limits = [400, 540, 120, 9]  # [water, milk, beans, cups]
        self.balance = 550
        self.state = self.CHOOSE_ACTION
        self.cur_ingredient = None  # counter for FILL command - 'secondary' state

    def show_status(self):
        print("\nThe coffee machine has:\n"
              + "\n".join(["{} of {}".format(x, y) for x, y in zip(self.limits, self.INGREDIENTS)])
              + f"\n${self.balance} of money")

    def sell_coffee(self, coffee_type):
        ingredients, cost = self.RECEIPTS[coffee_type - 1][1:3]
        new_limits = []

        for x, y in enumerate(self.limits):
            if y >= ingredients[x]:
                new_limits.append(y - ingredients[x])
            else:
                print(f"Sorry, not enough {self.INGREDIENTS[x]}!")
                break
        else:
            print("I have enough resources, making you a coffee!")
            self.limits = new_limits
            self.balance += cost

    def process_action_choice(self, action):
        if action == self.BUY:
            self.state = self.CHOOSE_COFFEE

        elif action == self.TAKE:
            print(f"I gave you ${self.balance}")
            self.balance = 0

        elif action == self.FILL:
            self.state = self.FILL_SUPPLIES
            self.cur_ingredient = 0
            print()

        elif action == self.REMAINING:
            self.show_status()

        elif action == self.EXIT:
            self.state = self.EXITING

    def process_fill_input(self, line):
        if line.isnumeric():
            self.limits[self.cur_ingredient] += int(line)

            if self.cur_ingredient + 1 >= len(self.limits):  # all ingredients were entered
                self.cur_ingredient = None
                self.state = self.CHOOSE_ACTION  # return to main screen
            else:
                self.cur_ingredient += 1  # next ingredient
        else:  # any text - repeat question
            print()

    def process_coffee_choice(self, line):
        if line.isnumeric():
            self.sell_coffee(int(line))
        else:  # 'back' or other text
            print()
        self.state = self.CHOOSE_ACTION

    def process_user_input(self, line):
        if self.state == self.CHOOSE_ACTION:
            self.process_action_choice(line)

        elif self.state == self.CHOOSE_COFFEE:
            self.process_coffee_choice(line)

        elif self.state == self.FILL_SUPPLIES:
            self.process_fill_input(line)

    def ask_user(self):
        if self.state == self.CHOOSE_ACTION:
            print("\nWrite action ({}):".format(", ".join(self.ACTIONS)))
        elif self.state == self.CHOOSE_COFFEE:
            print("\nWhat do you want to buy? "
                  + ", ".join(["{} - {}".format(x, r[0]) for x, r in enumerate(self.RECEIPTS, 1)])
                  + ", back - to main menu:")
        elif self.state == self.FILL_SUPPLIES:
            print(self.ING_QUESTIONS[self.cur_ingredient])

    def run_machine(self):
        while self.state != self.EXITING:
            self.ask_user()
            line = input()
            self.process_user_input(line)


cm = CoffeeMachine()
cm.run_machine()
