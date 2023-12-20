print("Welcome to Dream Pizza!")
print('\n')
print('What size of pizza would you like?')
print('\n')

print(' 1 - Small Pizza  = $8.99 \n 2 - Medium Pizza  = $17.99   \n 3 - Large Pizza  = $24.99')

User_Selection = input('Enter the name or number of the pizza you want to order:  ')

# Small Pizza ;
if User_Selection.isdigit() and int(User_Selection) == 1 or User_Selection.lower() == 'small pizza':
    print('Small Pizza selected.')
    small_pizza_pepper = str(input('Do you want to add peppers? (+$2)  Please enter Y or N.  '))
    if small_pizza_pepper.lower() == 'y':
        print('Peppers added.')
    elif small_pizza_pepper.lower() == 'n':
        print('Your pepper preference was not fulfilled.')

    # Small Pizza Payment ;
    pay_method1 = input('How would you like to make the payment? (There is an additional 10% fee for card payments.) \n 1 - Card Payment  \n 2 - Cash Payment   ')
    
    if pay_method1 == '1' or pay_method1.lower() == 'card payment':
        print('Card payment method selected. Redirecting to the payment page...')
        if small_pizza_pepper.lower() == 'y':
            small_pizza_pepper_total = 11.99
            print("Total amount  = $", small_pizza_pepper_total, ' Thank you for choosing Dream Pizza Deliveries!')
        elif small_pizza_pepper.lower() == 'n':
            small_pizza_no_pepper_total = 8.99
            print("Total amount  = $", small_pizza_no_pepper_total, ' Thank you for choosing Dream Pizza Deliveries!')
    elif pay_method1 == '2' or pay_method1.lower() == 'cash payment':
        print('Cash payment method selected. Redirecting to the payment page...')
        if small_pizza_pepper.lower() == 'y':
            small_pizza_pepper_total_cash = 11.99
            print("Total amount  = $", small_pizza_pepper_total_cash, ' Thank you for choosing Dream Pizza Deliveries!')
        elif small_pizza_pepper.lower() == 'n':
            small_pizza_no_pepper_total_cash = 8.99
            print("Total amount  = $", small_pizza_no_pepper_total_cash, ' Thank you for choosing Dream Pizza Deliveries!')

# Medium Pizza ;
elif User_Selection == '2' or User_Selection.lower() == 'medium pizza':
    print('Medium Pizza selected.')
    medium_pizza_pepper = str(input('Do you want to add peppers? (+$3)  Please enter Y or N.  '))
    if medium_pizza_pepper.lower() == 'y':
        print('Peppers added.')
    elif medium_pizza_pepper.lower() == 'n':
        print('Your pepper preference was not fulfilled.')

    # Medium Pizza Payment ;
    pay_method2 = input('How would you like to make the payment? (There is an additional 10% fee for card payments.) \n 1 - Card Payment  \n 2 - Cash Payment   ')
    if pay_method2 == '1' or pay_method2.lower() == 'card payment':
        print('Card payment method selected. Redirecting to the payment page...')
        if medium_pizza_pepper.lower() == 'y':
            medium_pizza_pepper_total = 20.99
            print("Total amount  = $", medium_pizza_pepper_total, ' Thank you for choosing Dream Pizza Deliveries!')
        elif medium_pizza_pepper.lower() == 'n':
            medium_pizza_no_pepper_total = 17.99
            print("Total amount  = $", medium_pizza_no_pepper_total, ' Thank you for choosing Dream Pizza Deliveries!')
    elif pay_method2 == '2' or pay_method2.lower() == 'cash payment':
        print('Cash payment method selected. Redirecting to the payment page...')
        if medium_pizza_pepper.lower() == 'y':
            medium_pizza_pepper_total_cash = 20.99
            print("Total amount  = $", medium_pizza_pepper_total_cash, ' Thank you for choosing Dream Pizza Deliveries!')
        elif medium_pizza_pepper.lower() == 'n':
            medium_pizza_no_pepper_total_cash = 17.99
            print("Total amount  = $", medium_pizza_no_pepper_total_cash, ' Thank you for choosing Dream Pizza Deliveries!')

# Large Pizza ;
elif User_Selection == '3' or User_Selection.lower() == 'large pizza':
    print('Large Pizza selected.')
    large_pizza_pepper = str(input('Do you want to add peppers? (+$3)  Please enter Y or N.  '))
    if large_pizza_pepper.lower() == 'y':
        print('Peppers added.')
    elif large_pizza_pepper.lower() == 'n':
        print('Your pepper preference was not fulfilled.')

    # Large Pizza Payment ;
    pay_method3 = input('How would you like to make the payment? (There is an additional 10% fee for card payments.) \n 1 - Card Payment  \n 2 - Cash Payment   ')
    if pay_method3 == '1' or pay_method3.lower() == 'card payment':
        print('Card payment method selected. Redirecting to the payment page...')
        if large_pizza_pepper.lower() == 'y':
            large_pizza_pepper_total = 27.99
            print("Total amount  = $", large_pizza_pepper_total, ' Thank you for choosing Dream Pizza Deliveries!')
        elif large_pizza_pepper.lower() == 'n':
            large_pizza_no_pepper_total = 24.99
            print("Total amount  = $", large_pizza_no_pepper_total, ' Thank you for choosing Dream Pizza Deliveries!')
    elif pay_method3 == '2' or pay_method3.lower() == 'cash payment':
        print('Cash payment method selected. Redirecting to the payment page...')
        if large_pizza_pepper.lower() == 'y':
            large_pizza_pepper_total_cash = 27.99
            print("Total amount  = $", large_pizza_pepper_total_cash, ' Thank you for choosing Dream Pizza Deliveries!')
        elif large_pizza_pepper.lower() == 'n':
            large_pizza_no_pepper_total_cash = 24.99
            print("Total amount  = $", large_pizza_no_pepper_total_cash, ' Thank you for choosing Dream Pizza Deliveries!')
