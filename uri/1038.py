x, y = input().split()

cod = int(x)
qty = int(y)

if cod == 1:
    print ("Total: R$ %.2f" %(qty*4.00))
elif cod == 2:
    print("Total: R$ %.2f"  %(qty*4.50))
elif cod == 3:
    print("Total: R$ %.2f"  %(qty*5.00))
elif cod == 4:
    print("Total: R$ %.2f"  %(qty*2.00))
elif cod == 5:
    print("Total: R$ %.2f"  %(qty*1.50))