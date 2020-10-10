print("BILL")
print('......................................................................')
D=int(input('Enter price 1:'))
E=int(input('Enter price 2:'))
F=int(input('Enter price 3:'))
G=int(input('Enter price 4:'))
Bill=(D+E+F+G)
print("Total: "),Bill
Discount=Bill*10/100
Final_Amount= Bill-Discount
if(Bill>100):
    print ("Discounted_Amount: "),Final_Amount
else:
    print("Final_Amount: "),Bill


