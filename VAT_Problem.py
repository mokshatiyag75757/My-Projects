print("VAT problem Difficulty: ★ Write a program that asks the user for a price of an item.  Include a function that returns the VAT for the item.  This should be output in the main program.")
def vat(hi):
    return hi * 0.05

price = float(input("Enter price: "))
v = vat(price)
print("VAT is:", v)
print()
print("Total cost:", v + price)
