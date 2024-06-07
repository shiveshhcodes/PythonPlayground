from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify (
            title = " REST NOW " ,
            message = "rest karle bhai" ,
            app_icon="/Users/shiveshrichhariya/Downloads/search.png",
            timeout=4,
        )
        time.sleep(10)