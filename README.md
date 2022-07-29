# Reaction-Time-Test-Bot
I've been known to have a slow reaction time, I did not like that, I wanted to get the best score possible so I created a bot in python to do the work for me

So in order to create this program, I first started off with getting the rgb values of the green colour that the website used when it indicated for the user to click. 
To do that I used a command **import pyautogui** followed by **pyautogui.displayMousePosition()** in a new IDLE Shell which allowed me to see the values directly.

Next I opened a new python idle file and imported the following libraries to run the code

**pyautogui**
**time**
**keyboard**
**random**
**win32api, win32con**  This one was for running the click methods since win32 is the fastest way for a simple program like this

Next I set up the click method which would set the cursor on the position to be clicked on and then click with a 0.01s release delay so that the click would register

Finally, I just checked the values of the rgb in that pixel to make sure that colour added up to be green
