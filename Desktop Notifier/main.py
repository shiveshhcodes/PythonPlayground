from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify (
            title = " REST NOW " ,
            message = "time for rest shivesh" ,
            # app_icon="/Users/shiveshrichhariya/Downloads/search.png",
            timeout=5,
        )
        time.sleep(10)