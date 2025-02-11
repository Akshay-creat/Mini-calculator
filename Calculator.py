print("---------Mini Calculator--------")

num1 = float(input("enter number 1 : "))
num2 = float(input("enter number 2: "))
print("Press 1 for additon\npress 2 for subtraction\npress 3 for multiplication\npress 4 for division")

choice = int(input("enter your choice from 1-4: "))
if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1/num2)
else:
    print("invalid")