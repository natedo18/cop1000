#Minh-Nhat Do 2418180
#Pseudocode
#start by setting base size of pattern,
#because final output wants to be 0-9, base size is 10
#set r to 0 for start
#set up loop to iterate as long as row is in range of BASE_SIZE
#set up column to print as long as row is in range
#print output as column as it is set to row+1
def main():
    BASE_SIZE=10 #setting base size
    row=0
    for row in range(BASE_SIZE):    #starting for loop
        for column in range(row+1): #set up inner loop
            print(column,end='')
        print()    
           
      
main()

#collaborators: none
