# Write your code here
coffee = (200, 50, 15)

limits = []

print("Write how many ml of water the coffee machine has:")
limits.append(int(input()))

print("Write how many ml of milk the coffee machine has:")
limits.append(int(input()))

print("Write how many grams of coffee beans the coffee machine has:")
limits.append(int(input()))

print("Write how many cups of coffee you will need:")
cups = int(input())

max_avail = min([limits[x] // y for x, y in enumerate(coffee)])
# print(max_avail)

if cups == max_avail:
    print("Yes, I can make that amount of coffee")
elif max_avail > cups:
    print("Yes, I can make that amount of coffee (and even {} more than that)".format(max_avail - cups))
else:
    plural = "s" if max_avail != 1 else ""
    print(f"No, I can make only {max_avail} cup{plural} of coffee")


# print(f"For {cups} cup{plural} of coffee you will need:")

# print("{} ml of water".format(cups * coffee[0]))
# print("{} ml of milk".format(cups * coffee[1]))
# print("{} g of coffee beans".format(cups * coffee[2]))

s = """Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!"""
