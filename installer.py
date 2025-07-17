import os, time
import winreg
import win32com.client
from datetime import datetime

def get_desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders')
    desktop, _ = winreg.QueryValueEx(key, 'Desktop')
    winreg.CloseKey(key)
    desktop = os.path.expandvars(desktop)
    return desktop
import os, time
import winreg
import win32com.client
from datetime import datetime

def get_desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders')
    desktop, _ = winreg.QueryValueEx(key, 'Desktop')
    winreg.CloseKey(key)
    desktop = os.path.expandvars(desktop)
    return desktop

def create_shortcut(target_path, shortcut_path, icon_path=None):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    if icon_path:
        shortcut.IconLocation = icon_path
    shortcut.save()
now = datetime.now()
temp = now.weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_sorted = ["Today", "Tomorrow"]
days.pop(temp)
if temp >= 5:
    days.pop(0)
else:
    days.pop(temp)
for day in days:
    if temp >= 4:
        temp = 0
        days_sorted.append(days[temp])
    else:
        temp += 1
        days_sorted.append(days[temp])
def clear():
    os.system("cls")
msg = []
printed = []
lines = ["1;\n", "2;\n", "3;\n", "4;\n", "5;\n", "6;\n", "7;"]
def check():
    if len(msg) not in printed:
        printed.append(len(msg))
        clear()
        for info in msg:
            print(info)
exists = False
while True:
    time.sleep(0.5)
    check()
    if len(msg) == 0:
        try:
            with open("toDo.cfg", "r", encoding="utf-8") as file:
                lines = file.readlines()
                msg.append("Config file allready exists...")
                exists = True
        except FileNotFoundError:
            msg.append("creating config file...")
            with open("toDo.cfg", "w", encoding="utf-8") as file:
                file.writelines(lines)
    elif len(msg) == 1:
        msg.append("config file created!")
    check()
    if len(msg) == 2:
        for i in range(4):
            clear()
            for info in msg:
                print(info)
            print(f"initializing {"." * i}")
            time.sleep(0.5)
        msg.append("temp")
        if exists == False:
            print("let's create your first plan!") 
            time.sleep(0.5)
    check()
    if len(msg) == 3:
        msg.pop(2)
        msg.append("initialized")
        planning = True
        clear()
        if exists == False:
            for i in range(7):
                planned = []
                plan = ""
                day = []
                def greet():
                    print(f"Let's plan {days_sorted[i]}:")
                if i == 0:
                    write = []
                    for letter in list("ex. $~ Chess rematch"):
                        clear()
                        greet()
                        write.append(letter)
                        print("".join(write))
                        if len(write) % 5 == 0:
                            time.sleep(0.6)
                        else:
                            time.sleep(0.2)
                    clear()
                    greet()
                    print("ex. $~ Chess rematch   |Written|")
                    print("Q to quit planning for current day")
                    time.sleep(0.5)
                    input("\ngot it? (Enter to proceed)")
                while plan.lower() != "q":
                    clear()
                    greet()
                    for temp in planned:
                        print(temp)
                    plan = input("$~ ")
                    if plan.lower() != "q" and plan != "":
                        planned.append(f"$~ {plan}  |Written|")
                        time.sleep(0.6)
                        day.append(f"{plan},")
                lines[i] = f"{i + 1};{"".join(day)}\n"
                with open("toDo.cfg", "w", encoding="utf-8") as file:
                    file.writelines(lines)
            empty = False
            for line in lines:
                try:
                    if line.split(f"{lines.index(line)};")[1] != "" and empty == False:
                        empty = False
                    else:
                        empty = True
                except IndexError:
                    empty = True
            if empty == False:
                msg.append("Scheme created")
            else:
                msg.append("Scheme creation skipped...")
        else:
            msg.append("Scheme allready exists...")
    check()
    if len(msg) == 4:
        try:
            with open("template.cfg", "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:           
            clear()
            template = ""
            templates = ["Enter as before\n"]
            print("Let's create your template (For day's without preplannig done)")
            time.sleep(1)
            templates_ = []
            while template.lower() != "q":
                clear()
                for temp in templates:
                    print(temp)
                template = input("$~ ")
                if template.lower() != "q" and template != "":
                    templates_.append(template + ",")
                    templates.append(f"$~ {template}  |Written|")
                    time.sleep(0.6)
            if len(templates_) != 0:
                msg.append("template created")
                templates_.pop(-1)
                with open("template.cfg", "w", encoding="utf-8") as file:
                    file.writelines(templates_)
            else:
                msg.append("template creation skipped...")
    else:
        msg.append("template already exists...")
    try:
        with open("start.cfg", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        now = datetime.now()
        date = str(now).split(" ")[0]
        with open("start.cfg", "w", encoding="utf-8") as file:
            file.write(date)
    check()
    if len(msg) == 5:
        msg.append("Downloading main script")
        os.system("curl https://raw.githubusercontent.com/todo-temp/temp/main/main.py -o main.py")
    check()
    if len(msg) == 6:
        msg.append("Creating Symlink")
        current_dir = os.getcwd()
        exe_name = "main.py"
        target_exe = os.path.join(current_dir, exe_name)

        if not os.path.isfile(target_exe):
            print(f"error has occured!")
            exit(1)
        desktop_path = get_desktop_path()
        shortcut_name = "ToDo-app.lnk"
        shortcut_file = os.path.join(desktop_path, shortcut_name)
        create_shortcut(target_exe, shortcut_file)
        
    check()
    if len(msg) == 7:
        msg.append("Creating specialized dir")
        os.system("mkdir weeks")
    if len(msg) == 8:
        os.system('echo Set objShell = CreateObject("WScript.Shell") > completed.vbs')
        os.system('echo objShell.Popup "installation completed!", 0, "Info", 64 >> completed.vbs')
        os.system("completed.vbs")
        time.sleep(3)
        os.system("del completed.vbs")
        os.system("del installer.py")
        break

    
