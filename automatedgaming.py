#importing libraries
from PIL import ImageGrab , ImageOps
from numpy import array
import pyautogui
import time


#using the cordinates for the repalybutton and the cordinates of the dinasour
#for the sake of the convinience
class Cordinates():
    replayBtn = (337, 349)
    dinasour = (182, 354)

#   Function to restart Game:
def restartGame():
    pyautogui.click(Cordinates.replayBtn)

#   Function to make the character jump
def jump():
    pyautogui.keyDown('space')
    time.sleep(0.15)
    pyautogui.keyUp('space')

#   Getting the Exact Cordinates of the box to tell the character where --
#   -- to jump
def imageGrab():
    image = ImageGrab.grab((232, 356,290, 371))
    #   Converting the RGB to GrayScale
    grayimage = ImageOps.grayscale(image)
    #   Obtaining the Array of GrayScale Image
    a = array(grayimage.getcolors())
    #   Checing the sum of the Array
    return a.sum()

#just for the Sake of Convinience
time.sleep(.8)
add = imageGrab()
print('Value of the small block is used')


#   Main function
def main():

    restartGame()
    #loop will run continiously 
    while True:
        #   Printing the values of the imageGrab (sum of the Array):
        print(imageGrab())
        #   If the ImageGrab not equal to the add of the image cropped
        #   -- then the character will jump
        if(imageGrab() != add):
            jump()

    # End of the main loop: ----

#   Executing the main function:
main()
