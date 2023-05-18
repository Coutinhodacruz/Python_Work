from AtmMachine.Account import Accounts


def Main():
    accounts = []
    accountNumber = Accounts()
    # for i in range(10):
    #     accounts.append(Accounts)

    while True:
        id = eval(input("Enter account ID: "))

        if 0 <= id <= 9:

            print()
            print("Main menu")
            print("1: check balance")
            print("2: withdraw")
            print("3: deposit")
            print("4: exit")
            print()

            menuChoice = eval(input("Enter choice: "))
            print()

            while menuChoice != 4:
                if menuChoice == 1:
                    balance = accountNumber.getBalance()

                    print("The balance is ", balance)
                    menuChoice = prints(menuChoice)

                elif menuChoice == 2:
                    withdrawalAmount = eval(input("Enter withdrawal amount: "))
                    accountNumber.withdrawal(withdrawalAmount)
                    menuChoice = prints(menuChoice)

                elif menuChoice == 3:
                    depositAmount = eval(input("Enter your deposit amount: "))
                    accountNumber.setBalance(depositAmount)
                    menuChoice = prints(menuChoice)

                elif menuChoice == 4:
                    exit = menuChoice

                    print(quit())
                else:
                    menuChoice = eval(input("Please enter a valid menu choice (1-4): "))
                    print()

        else:
            print("Account ID must be a number between 0 and 9. Please try again.")
            print()


def prints(menuChoice):
    print()
    print("Main menu")
    print("1: check balance")
    print("2: withdraw")
    print("3: deposit")
    print("4: exit")
    print()
    menuChoice = eval(input("Enter a choice: "))
    print()
    return menuChoice


Main()
