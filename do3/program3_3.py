#Minh-Nhat Do 2418180
#Pseudocode
#prompt a user for the input of an odd integer between 50 and 100
#assign input to integer
#use logical operator, and, to check that input is between 50 and 100
#check for even or odd by using %2 operator
#using %2 divides input by 2 while leaving the reaminder
#setting that expression to check if it is equal to 1 will allow you to test for odd integers
#setting it equal to 0 would test for even, since there would be no remainder
#display the results accordingly
def main():
#prompt input from the user    
    integer=int(input('Input an odd integer between 50 and 100: '))
#by setting condition to have the reaminder equal 1 tests for odd integer input
#setting remainder to equal 0 would test for even number    
    if ((integer>=50 and integer<=100) and (integer%2==1)):
        print('Correct!')
    else:
        print('Incorrect')
main()
#collaborators: none
