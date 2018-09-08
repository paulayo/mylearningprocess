# you can use a for loop
# inside a while loop
# and a while loop inside
# a for loop

print('Welcome to Iron Bank of Bravoos ATM')
restart = ('Y')
chances = 3
balance = 67.14
while chances >= 0:
    pin = int(input('Please Enter Your 4 Digit pin: '))
    if pin == (1234):
        print('You entered your pin correctly\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdrawl\n')
            print('Please Press 3 To Pay in\n')
            print('Please Press 4 To Return Card\n')
            option = int(input('What Would you like to choose?'))
            if option == 1:
                print('Your Balance is AE', balance,'\n')
                restart = input('Would You like to go back?')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? \nAE10/AE20/AE40/AE60/AE80/AE100'))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print('\nYour Balance is now AE',balance)
                    restart = input(('Would You like to go back? '))
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount'))

            elif option == 3:
                Pay_in = float(input('How Much Would You Like To Pay In? '))
                balance = balance + Pay_in
                print('\nYour Balance is now AE',balance)
                restart = input('Would You like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break

            elif option == 4:
                print('Please wait whilst your card is Returnes...\n')
                print('Thank you for your service')
                break
            else:
                print('Please Enter a correct number, \n')
                restart = ('y')
    else:
        pin != ('1234')
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break



