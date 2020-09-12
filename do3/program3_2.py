#Minh-Nhat Do 2418180
#Pseduocode
#prompt user to enter their age, assign to variable, age
#use if expressions to test age value
#if age is larger than 19, display, you are an adult
#if age is smaller than 13, display, you are a minor
#if neither of those conditions is met, display, you are a teenager
def main():
    age=int(input('Enter your age: '))  #prompt for age from user
    if age>19:                          #display appropriate response based on age
        print('You are an adult.')
    elif age<13:
        print('You are a minor.')
    else:
        print('You are a teenager.')
main()
#collaborators: none
