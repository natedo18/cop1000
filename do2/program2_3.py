#2418180
#Pseudocode
#display message prompting input of three dimensions with variables to
#length, width, and height
#calculte the volume 
#calculate the surface area
#display calculations with correct formatting to two decimal places

#dimensions input by user
length=float(input('Input the length of the box using decimals as neccessary: '))
width=float(input('Input the width of the box using decimals as neccessary: '))
height=float(input('Input the height of the box using decimal points as neccessary: '))
#calculate the total volume of the box
volume=length*width*height
#calculate the surface area of the box
surfaceArea=((width*height)*2.0)+((width*length)*2.0)+((height*length)*2.0)
#display volume to two decimal places with formatting
print(format(volume,'.2f'))
#display
print(format(surfaceArea,'.2f'))


#Collaborators: none
