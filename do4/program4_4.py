#Minh-Nhat Do 2418180
#Pseudocode
#set accumulator, assign to total
#set constants of minimum integer to 100, assign to MIN
#set integer to be MIN, in order to add one each time
#to continue the loop
#set while loop to continue as long as total is less than 500
#use if statement to check for integer is mulitple of 13
#by setting to check if integer divided by 13 is 0
#otherwise, integer is not a multiple of 13
#if it is, add to the total,
#if not, 1 gets added to integer and the loop restarts
#once total>=500, multiples get printed


def main():
    total=0     #start accumulator
    MIN=100     #set starting intger number
    integer=MIN
    while total<500:    #while loop started with condition of being <500
        if integer%13==0:   #checks if integer is a multiple of 13
            total+=integer  #if it is, integer gets added to total
        
            print(integer,end=' ')  #print multiples of thirteen, use end=' ' to seperate
                                    #each multiple with a space
        integer+=1                  #make sure to use a space in the item specifier 
                
main()        


#collaborators: none
