import pyautogui
import random 



import time
x=["0","o","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","x","y","w","v","t"]
y= int(input("Enter the number of times u want to loop : "))
#(x=600, y=148)
#print(pyautogaui);

for i in range(0,y):                
    pyautogui.click(680,160)
    pyautogui.typewrite(random.choice(x))
    pyautogui.hotkey("enter")
    time.sleep(.5)