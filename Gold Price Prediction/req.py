import requests
import time

url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSchWIEPVC-JDe4lQ5dm_vhwQSd0kwj2WDpQdEBsJyfQz1pwkw/formResponse"


def send_attendance(url):
    try:
        while True:
            requests.post(url)
            print("Form Submitted.")
    except:
        print("Error Occured!")


send_attendance(url)
