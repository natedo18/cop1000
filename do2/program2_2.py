#2418180
#Pseudocode
#Display message prompting input of seconds over 500
#calculate time in minutes and seconds using the remainder operative
#display calculations

#input of total seconds by user
totalSeconds=float(input('Input number of seconds over 500: '))
#calculating minutes and seconds using remainder operative
minutes=(totalSeconds//60)%60
seconds=totalSeconds%60
print('Here is the time in minutes, and seconds: ')
print('Minutes:',minutes)
print('Seconds:',seconds)

#Collaborators: none
