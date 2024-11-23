print("Select your ride:")
print("1. Car")
print("2. Bike")
ridechoice = int(input("Enter 1 or 2"))

if ridechoice == 1:
    
    print("Select your car :")
    print("1. Thar Roxx Mx5")
    print("2. Thar Roxx AX7L")
    carchoice = int(input("Enter 1 or 2"))
    if carchoice == 1:
        print("16.99 lakhs")
    elif carchoice == 2:
        print("18.99 lakhs")

elif ridechoice == 2:
    
    print("Select your bike ")
    print("1. Freedom 125 CNG")
    print("2. Pulsar N125")
    bikechoice = int(input("Enter 1 or 2"))
    if bikechoice == 1:
        print("1.10 lakhs")
    elif bikechoice == 2:
        print("85,000 rupees")