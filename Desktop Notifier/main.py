# sends desktop notification time to time, on input command accordingly.

from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify (
            title = " REST NOW " ,
            message = "Rest Time Dudeeeeee!!" ,
            # app_icon="/Users/shiveshrichhariya/Downloads/search.png",
            timeout=5,
        )
        time.sleep(10)