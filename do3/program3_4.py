#Minh-Nhat Do 2148180
#Pseudocode
#ask the user for the answers to three different questions
#one answer will be of type int
#one answer will be of type float
#one answer will be of type str
#use elif expressions to display correct or incorrect

def main():
#prompting question 1 with int type as an answer
    year=int(input('What year did COIVD-19 force the United States to almost shut down '\
                   'and encourage everyone to qurantine and keep their distance? '))
    if year==2020:
        print('Correct!')
    else:
        print('Incorrect.')
#prompting question 2 with float type as an answer
    area=float(input('What is the area of a rectangle that has a height of 26.3 and a width '\
                     'of 15.4? Round to the nearest hundreth. '))
    if area == 405.02:
        print('Correct!')
    else:
        print('Incorrect')
#prompting question 3 with str type as an answer
    code=str(input('What coding language was this quiz built with? '))
    if code=='Python' or code=='python':     #use or operator to disregard capitalization errors
        print('Correct!')
    else:
        print('Incorrect')
main()

#collaborators: none
