#!/usr/bin/env python
#this is the library needed
from sense_hat import SenseHat
from time import sleep
import time

#setting a variable to call for SenseHat
sense = SenseHat()

#Number that will be displayed on Matrix from 0 to 9 (this is a list)
numberDisplay = [
[[0,1,1,1], # Zero
[0,1,0,1],
[0,1,0,1],
[0,1,1,1]],
[[0,0,1,0], # One
[0,1,1,0],
[0,0,1,0],
[0,1,1,1]],
[[0,1,1,1], # Two
[0,0,1,1],
[0,1,1,0],
[0,1,1,1]],
[[0,1,1,1], # Three
[0,0,1,1],
[0,0,1,1],
[0,1,1,1]],
[[0,1,0,1], # Four
[0,1,1,1],
[0,0,0,1],
[0,0,0,1]],
[[0,1,1,1], # Five
[0,1,1,0],
[0,0,1,1],
[0,1,1,1]],
[[0,1,0,0], # Six
[0,1,1,1],
[0,1,0,1],
[0,1,1,1]],
[[0,1,1,1], # Seven
[0,0,0,1],
[0,0,1,0],
[0,1,0,0]],
[[0,1,1,1], # Eight
[0,1,1,1],
[0,1,1,1],
[0,1,1,1]],
[[0,1,1,1], # Nine
[0,1,0,1],
[0,1,1,1],
[0,0,0,1]]
]

#a display to show that the number doesn't exist
noNumberDisplay = [0,0,0,0]

#The color of the time for hour and minute
hourHandColor = [255,0,0] # Red
minuteHandColor = [0,255,255] # Cyan
emptyColor = [0,0,0] # Black/Off

#Setting this to an empty array to use it for larger array to be pushed in here
clockImage = []

#using the localtime hour that is packaged within the library from time.
hour = time.localtime().tm_hour
minute = time.localtime().tm_min

#This for loop, and within a for loop is an If condition for setting up time
#The algorithm is started when we insert a row of 4 elements on the for loop,
#from each number in a single call, this saves us having to run two concurrent loops.
#In a two-digit number, we use a division by 10 to retrieve the first number. 
#For example we use the # 12, we would get 1 from a division by 10.
#To get the second digit we make use of modulus which returns us the remainder from a division, 
#so in this case from our previous selection for 12 we will get the return of 2.

for index in range(0, 4):
  #In this If loop, we use the .extend function to create a list
    if (hour >= 10):
        clockImage.extend(numberDisplay[int(hour/10)][index])
    else:
        clockImage.extend(noNumberDisplay)
    clockImage.extend(numberDisplay[int(hour%10)][index])

#Same thing what we did for hour is what we will do for minute 
for index in range(0, 4):
    clockImage.extend(numberDisplay[int(minute/10)][index])
    clockImage.extend(numberDisplay[int(minute%10)][index])
    
#Now we have our final 'for' loop the entire clockImage array, this loop is designed to swap 
#out of every number with our RGB values. We achieve this by just checking whether
#there is a number 0 or 1 inside that index. If it’s 0 we output our empty variable value
#to that number. Otherwise, we check to see if we are dealing with the first 32 pixels 
#(which is the top half of the LED matrix), if we are in the top half we grab the RGB values 
#from our hourColor variable. Otherwise, we utilize the RGB values from the minuteColor variable.

for index in range(0, 64):
    if (clockImage[index]):
        if index < 32:
            clockImage[index] = hourHandColor
        else:
            clockImage[index] = minuteHandColor
    else:
        clockImage[index] = emptyColor

#In a While Loop what is being continued till we manuelly exit it. 

while True:
  sense.set_rotation(270) #the rotation for sensehat display
  temp = sense.get_temperature() #obtaining the temperature # from the sensor
  temp = round(((temp/5)*9)+32) #rounding and converting the celcius to fehrenheit
  sense.show_message("%.1f F" % temp) #Display a message on the sensehat to show temperature (%.1f)
  sense.set_pixels(clockImage) #calling in the clockImage to display the result.
  sleep(10) #Calling in to sleep or what you call a delay for 10 sec.
