print("Enter customer name:", end=" ")
customer = input()

print("Enter Item 1 name:", end=" ")
item1 = input()
print("Enter Item 1 price:", end=" ")
price1 = float(input())

print("Enter Item 2 name:", end=" ")
item2 = input()
print("Enter Item 2 price:", end=" ")
price2 = float(input())

print("Enter Item 3 name:", end=" ")
item3 = input()
print("Enter Item 3 price:", end=" ")
price3 = float(input())

total = price1 + price2 + price3
gst = total * 0.05
final_amount = total + gst

print("==================================================")
print("                BILL RECEIPT")
print("==================================================")
print("Customer Name :", customer)
print("--------------------------------------------------")
print("Item\t\tPrice (Rs.)")
print(item1, "\t\t", price1)
print(item2, "\t\t", price2)
print(item3, "\t\t", price3)
print("--------------------------------------------------")
print("Total Amount :", total)
print("GST (5%)     :", gst)
print("Final Amount :", final_amount)
print("==================================================")
