#Minh-Nhat Do 2418180
#Pseudocode
#start by assigning constants to REDUCTION (.25), TAX (0.07)
#prompt the user to input the ticket price item and assign to variable, price
#prompt the user to input whether item is on sale or not
#if the item is on sale, multiply by .25 to get amount reduced,
#assign to discount
#calculate sale price by subtracting discount from price,
#assign to variable, sale_price
#if the item is not reduced, assign price as sale_price
#prompt the user to input whether item is taxable or not
#if the item is taxable, multiply sale_price by 0.07 to calculate sales tax,
#assign to variable sales_tax
#if the item is not taxable, assign sales_tax as 0.00
#to calculate the total amount due, assign sale_price+sales_tax to total
#print all required information
def main():
#assign constants for sale reduction and tax
    REDUCTION=0.25
    TAX=0.07
#prompt input of ticket price from the user,
#use float in case an item is not a whole dollar
    price=float(input('Enter the ticket price of the item: '))
#determine if the item is reduced and calculate sale price as needed
    reduced=input('Is this item reduced y/n? ')
    if reduced=='y':
        discount=(price*REDUCTION)
        sale_price=(price-discount)
    else:
        discount=0                          #if item is not on sale,
        sale_price=price                    #assign price to sale_price

#determine if the item is taxable and calculate tax as needed
    taxable=input('Is this item taxable y/n? ')
    if taxable=='y':
        sales_tax=sale_price*TAX
    else:
        sales_tax=0                          #sales_tax set to 0 if item is not
#assign final price of the item to total     #taxable
    total=(sale_price+sales_tax)
#printing all required information                         
    print('Here is your bill:')
    print('Original price: $',format(price,'.2f'),sep='')
    print('Reduction during event: $',format(discount,'.2f'),sep='')
    print('Final price: $',format(sale_price,'.2f'),sep='')
    print('7% Sales tax: $',format(sales_tax,'.2f'),sep='')
    print('Total amount due: $',format(total,'.2f'),sep='')
main()

#collaborators: none
