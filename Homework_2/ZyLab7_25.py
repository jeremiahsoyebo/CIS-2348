# Jeremiah Soyebo - 1902930 #

def exact_change(user_total):
    num_dollars = user_total // 100  # get dollars #
    user_total %= 100
    num_quarters = user_total // 25  # get quarters #
    user_total %= 25
    num_dimes = user_total // 10  # get dimes #
    user_total %= 10
    num_nickels = user_total // 5  # get nickels #
    user_total %= 5
    num_pennies = user_total  # use left over for pennies #
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

if __name__ == '__main__':
    user_total = int(input())  # get user input #
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(user_total)

if user_total <= 0:
    print('no change')
else:
    if num_dollars > 1:  # format dollars #
        print(num_dollars, 'dollars')
    elif num_dollars == 1:
        print(num_dollars, 'dollar')

    if num_quarters > 1:  # format quarters #
        print(num_quarters, 'quarters')
    elif num_quarters == 1:
        print(num_quarters, 'quarter')

    if num_dimes > 1:  # format dimes #
        print(num_dimes, 'dimes')
    elif num_dimes == 1:
        print(num_dimes, 'dime')

    if num_nickels > 1:  # format nickels #
        print(num_nickels, 'nickels')
    elif num_nickels == 1:
        print(num_nickels, 'nickel')

    if num_pennies > 1:  # format pennies #
        print(num_pennies, 'pennies')
    elif num_pennies == 1:
        print(num_pennies, 'penny')
# not sure why I can't run the last 2 in zyBooks #
