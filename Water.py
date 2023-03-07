import time
from plyer import notification

if __name__ == "__main__":
    while True:
        
        notification.notify(
            title = "Please Have Water Now!",
            message = "A general rule of thumb for healthy people is to drink two to three cups of water per hour, or more if you're sweating heavily",
            app_icon = "Assets/Glass-Water-icon.ico",
            timeout = 10
            
            )
        
        time.sleep(60*60)