'''
This program implements a checkout system that fulfills the following requirements.

1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples

Author: Aditya Dubal
Language: Python (2.7)
'''

import sys

# Function to calculate price of Coffee
def calculate_coffee(count):
    cof_price = 0.0
    global product_price
    if count % 2 == 0:
        print '%12s' % "BOGO" + '%11s' % (-1*(product_price.get('CF1')))
        cof_price += 0
    else:
        cof_price += product_price.get('CF1')
    return cof_price


# Function to calculate price of Chai
def calculate_chai():
    ch_price = 0.0
    global milk_price, milk_count, chai_count, product_price
    ch_price += product_price.get('CH1')
    # Check if there is already milk in basket
    if milk_count >= 1:
        milk_price += special_case_chai(chai_count, milk_count)
    return ch_price


# Case where in Chai comes after Milk
def special_case_chai(chai_ct, milk_ct):
    mk_price = 0.0
    global product_price
    if chai_ct >= 1:
        if milk_ct == chai_ct or milk_ct > chai_ct:
            print '%12s' % "CHMK" + '%11s' % (-1 * (product_price.get('MK1')))
            mk_price -= product_price.get('MK1')
        elif chai_ct > milk_ct:
            mk_price -= 0.0
    return mk_price


# Function to calculate price of Milks
def calculate_milk(milk_ct, chai_ct):
    mk_price = 0.0
    global product_price
    mk_price += product_price.get('MK1')
    if chai_ct >= 1:
        if milk_ct == chai_ct or chai_ct > milk_ct:
            print '%12s' % "CHMK" + '%11s' % (-1 * (product_price.get('MK1')))
            mk_price -= product_price.get('MK1')
        elif milk_ct > chai_ct:
            mk_price -= 0.0
    return mk_price


# Function to calculate price of Oatmeals
def calculate_oatmeal():
    ot_price = 0.0
    global apple_price, apple_count, oatmeal_count, product_price
    ot_price += product_price.get('OM1')
    # Check if there is already Apple in basket
    if apple_count >= 1:
        apple_price += special_case_oatmeal(oatmeal_count, apple_count)
    return ot_price


# Case where in Oatmeal comes after Apple
def special_case_oatmeal(oatmeal_ct, apple_ct):
    ap_price = 0.0
    global product_price
    if oatmeal_ct >= 1:
        if apple_ct == oatmeal_ct or apple_ct > oatmeal_ct:
            print '%12s' % "APOM" + '%11s' % (-1 * (product_price.get('AP1') / 2.0))
            ap_price -= 0.5 * (product_price.get('AP1'))
        elif oatmeal_ct > apple_ct:
            ap_price -= 0.0
    return ap_price


# Function to calculate price of Apples
def calculate_apple(oatmeal_ct, apple_ct):
    ap_price = 0.0
    global product_price
    if oatmeal_ct >= 1:
        if apple_ct == oatmeal_ct or oatmeal_ct > apple_ct:
            print '%12s' % "APOM" + '%11s' % (-1 * (product_price.get('AP1')/2.0))
            ap_price += 0.5 * (product_price.get('AP1'))
        elif apple_ct > oatmeal_ct:
            ap_price += oatmeal_ct * (product_price.get('AP1')/2.0)
    else:
        ap_price += product_price.get('AP1')
    return ap_price


def main(basket):
    print "Item" + '%20s' % "Price"
    print "-----" + '%19s' % "-----"
    global product_price, chai_count, apple_count, coffee_count, oatmeal_count, milk_count
    global coffee_price, chai_price, oatmeal_price, milk_price, apple_price

    # Key-value pair dictionary to save prices of products
    product_price = {'CH1': 3.11, 'AP1': 6.00, 'CF1': 11.23, 'MK1': 4.75, 'OM1': 3.69}

    # Variables initialization
    chai_count, apple_count, coffee_count, oatmeal_count, milk_count = 0, 0, 0, 0, 0
    coffee_price, chai_price, oatmeal_price, milk_price, apple_price = 0.0, 0.0, 0.0, 0.0, 0.0

    for item in basket:
        if item == 'CH1':
            chai_count += 1
            print "CH1" + '%20s' % (product_price.get('CH1'))
            chai_price += calculate_chai()
        elif item == 'CF1':
            coffee_count += 1
            print "CF1" + '%20s' % (product_price.get('CF1'))
            coffee_price += calculate_coffee(coffee_count)
        elif item == 'OM1':
            oatmeal_count += 1
            print "OM1" + '%20s' % (product_price.get('OM1'))
            oatmeal_price += calculate_oatmeal()
        elif item == 'MK1':
            milk_count += 1
            print "MK1" + '%20s' % (product_price.get('MK1'))
            milk_price += calculate_milk(milk_count, chai_count)
        elif item == 'AP1':
            apple_count += 1
            print "AP1" + '%20s' % (product_price.get('AP1'))
            apple_price += calculate_apple(oatmeal_count, apple_count)
        else:
            print "Wrong item! Enter valid item.."

    # APPL rule - If you buy 3 or more bags of Apples, the price drops to $4.50.
    if apple_count >= 3:
        new_price = 4.50 * apple_count
        # Providing best discount to customer
        apple_price = min(new_price, apple_price)

    total_price = chai_price + coffee_price + oatmeal_price + milk_price + apple_price
    print "----------------------------"
    print "Total:" + '%17s' % total_price
    return round(total_price, 2)

if __name__ == '__main__':
    # If function is called from Test file
    if len(sys.argv) > 1:
        main()
    else:
        # If this code file is executed independently
        data = raw_input("Enter items in basket: ").split(',')
        main(data)
