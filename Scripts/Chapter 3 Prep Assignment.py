#Minh-Nhat Do COP1000 Section 2213
#prompt input of amount of coffee ordered by user
#assign to variable coffee_ordered
#assign constants to price of coffee by weight
#FORTY_LBS, TWENTY_LBS, TEN_LBS, ONE_TO_NINE_LBS
#assign constants to tax, shipping
#TAX, SHIPPING
#calculate price of coffee with elif statements
#assign cost of coffee to variable, coffee_cost
#print final sale details

#assigning constants for price of coffee
FORTY_LBS=7.50
TWENTY_LBS=8.75
TEN_LBS=10.00
ONE_TO_NINE_LBS=12.00
#calculating price of coffee and assign to variable based on amount ordered
coffee_ordered=int(input('How many pounds of coffee are you ordering? '))
if coffee_ordered>=40:
    coffee_cost=coffee_ordered*FORTY_LBS
    print('Cost of cofee: $',format(coffee_cost,'.2f'),sep='')
elif coffee_ordered>=20:
    coffee_cost=coffee_ordered*TWENTY_LBS
    print('Cost of coffee: $',format(coffee_cost,'.2f'),sep='')
elif coffee_ordered>=10:
    coffee_cost=coffee_ordered*TEN_LBS
    print('Cost of coffee: $',format(coffee_cost,'.2f'),sep='')
else:
    coffee_cost=coffee_ordered*ONE_TO_NINE_LBS
    print('Cost of coffee: $',format(coffee_cost,'.2f'),sep='')
#assigning constants for tax and shipping
TAX=0.07
SHIPPING=1.00
#calculate and display sales tax for the order
sales_tax=coffee_cost*TAX
print('7% sales tax: $',format(sales_tax,'.2f'),sep='')
#calculate shipping for the order
if coffee_cost>150:
    shipping=coffee_ordered*0
    print('Shipping fee: $',format(shipping,'.2f'),sep='')
else:
    shipping=coffee_ordered*1
    print('Shipping fee: $',format(shipping,'.2f'),sep='')
#display final total due
print('Total payable: $',format(coffee_cost+sales_tax+shipping,'.2f'))

#Collaborators: None
