# Simple ATM Simulator
correct_pin = int(input("Enter Your pin : "))
balance = 5000.0
def check_balance():
    print("\n--- Balance ---")
    print(f"Your current balance is: ₹{balance:.2f}")
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
        print(f"New balance: ₹{balance:.2f}")
    else:
        print("Invalid amount!")
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Remaining balance: ₹{balance:.2f}")
print("********************************")
print("       SIMPLE ATM SIMULATOR       ")
print("********************************")
pin = input("Enter your 4-digit PIN: ")
if pin == correct_pin:
    print("\nLogin successful!")
    print("Welcome to the ATM.")
    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("==============================")
        choice = input("Enter your choice: ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("\nThank you for using the ATM!")
            print("Please collect your card.")
            break
        else:
            print("Invalid choice! Please try again.")
else:
    print("\nIncorrect PIN!")
    print("Access denied.")
