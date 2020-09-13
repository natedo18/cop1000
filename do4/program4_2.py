#Minh-Nhat Do 2418180
#Pseudocode
#assign coversion rate of inches to centimeters as constant, CONVERSION
#display column titles using \t escape character to move each title
#over to next tab
#use a for loop and range function to calculate conversion of
#inches to centimeters
#display and format table with results

def main():
    CONVERSION=2.54 #set conversion factor to constant
    print('INCHES\t CM') #display column headers using \t to move over one tab
    print('------\t --')
    for inches in range(1,13): #set highest range to 13 so program displays up to 12
        cm=inches*CONVERSION    #calculate cm per inch by multiplying by conversion factor
        print(format(inches,'4.1f'),format(cm,'7.2f')) #display and format results
main()        
        
#collaborators: online research for in to cm conversion
