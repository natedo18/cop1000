#2418180
#Pseudocode
#assign commission rate to constant, commission
#prompt input of selling prices of three cars
#assign to variables car1, car2, and car3
#calculate total sales and commission
#display values using format(value,'.2f'),'$',sep=''

#assign commission rate to constant
COMMISSION=0.035
#prompt input of selling prices
car1=float(input('Enter selling price of car 1: '))
car2=float(input('Enter selling price of car 2: '))
car3=float(input('Enter selling price of car 3: '))
#calculate commission total on each sale
commission=(car1*COMMISSION)+(car2*COMMISSION)+(car3*COMMISSION)
#calculate total sales
totalSales=(car1+car2+car3)
#display calculations
print('Here are your total sales:','$',format(totalSales,',.2f'),sep='')
print('Here is your commission:','$',format(commission,',.2f'),sep='')

#Collaborators: none
