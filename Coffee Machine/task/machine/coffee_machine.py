# Write your code here
coffee = (200, 50, 15)

print("Write how many cups of coffee you will need:")
cups = int(input())
plural = "s" if cups != 1 else""

print(f"For {cups} cup{plural} of coffee you will need:")

print("{} ml of water".format(cups * coffee[0]))
print("{} ml of milk".format(cups * coffee[1]))
print("{} g of coffee beans".format(cups * coffee[2]))

s = """Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!"""
