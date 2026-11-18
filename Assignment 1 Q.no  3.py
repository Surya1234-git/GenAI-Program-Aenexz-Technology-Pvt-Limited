amount = float(input("Enter order amount: "))
member = input("Are you a member (yes/no): ").strip().lower()

if amount < 0 or amount > 100000:
    print("Invalid order amount")
else:
    if amount >= 5000:
        discount_percent = 15
        status = "Eligible for 15% discount"
    elif member == "yes" and amount >= 2000:
        discount_percent = 10
        status = "Eligible for 10% member discount"
    else:
        discount_percent = 0
        status = "Not eligible for any discount"

    discount = amount * discount_percent / 100
    final_amount = amount - discount

    print("Original amount:", amount)
    print("Discount amount:", discount)
    print("Final payable amount:", final_amount)
    print("Status:", status)
