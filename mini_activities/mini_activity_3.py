price = float(input("Price in dollars: "))
taxRatePercent = int(input("Tax rate as a percent: "))

taxRate = taxRatePercent / 100
tax = price * taxRate
total = tax + price

print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")