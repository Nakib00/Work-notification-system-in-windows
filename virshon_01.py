#Work notification system in windows 
import time
from plyer import notification # Go Terminal and write "pip install plyer"

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "please Chack you have work", #write your Tital
            message = "Hello boss this is time to you drink water and eat some snacks", #write yor message
            timeout = 10  #notification live 10s

        )
        time.sleep(60*60) # it reminde you One houre to One houre 

# If you want run your computer perment,than go to Terminal and write "pythonw"