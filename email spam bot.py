import pyautogui
import time
#Giving the user time to open the browser
time.sleep(3)
#Using the shortcut to open a new tab
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/?tab=rm&authuser=0&ogbl")
pyautogui.press("enter")
for i in range(10):
    pyautogui.moveTo(100,250)
    time.sleep(15)
    pyautogui.click()
    time.sleep(10)
    #Writing the email address we want to send the email to and yes i know i spelled address wrong
    pyautogui.write("dillpickles432@gmail.com")
    time.sleep(5)
    pyautogui.moveTo(1700, 700)
    pyautogui.click()
    time.sleep(2)
    #Writing the body of the email
    pyautogui.write("Email spam bot")
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("enter")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("enter")
    time.sleep(15)
    #You dont need to put time delays that large only reason i did it was because my computer is a bit slow so you can adjust the time limits
