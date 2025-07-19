import os
from datetime import datetime
import time
import sys
def clear():
    os.system("cls")
os.system(r"cd %appdata%\\Todo-app\\")
try:
    with open("toDo.cfg.next", "r", encoding="utf-8") as file:
        file.readlines()
except FileNotFoundError:
    with open("toDo.cfg.next", "w", encoding="utf-8") as file:
        file.write("1;\n2;\n3;\n4;\n5;\n6;\n7;") 

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
now = datetime.now()
year = int(str(now).split(" ")[0].split("-")[0])
month = int(str(now).split(" ")[0].split("-")[1])
day = str(now).split(" ")[0].split("-")[2]
weekday = days[now.weekday()]
try:
    with open("free-time.cfg", "r", encoding="utf-8") as file:
        line = file.readlines()[0]
    if str(line.strip()) != str(now).split(" ")[0]:
        os.remove("free-time.cfg")
except FileNotFoundError:
    pass
with open("start.cfg", "r", encoding="utf-8") as file:
    line = str(file.readlines()[0])
count = 0
rounds = 0
if year % 4 == 0:
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
else:
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
while year != int(line.split("-")[0]):
    rounds += 1
    if year % 4 == 0:
        months = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if rounds >= 2:
        for num in months:
            count += num
    else:
        rounds = 0
        while month != 1:
            rounds += 1
            if rounds >= 2:
                count += months[month - 1]
            else:
                count += int(day)
            month -= 1
        count += 1  
    year -= 1  
if rounds >= 1:
    month = 12
    day = 31 
    count += 30
rounds = 0
while month != int(line.split("-")[1]):
    rounds += 1
    month -= 1
    if rounds >= 2:
        count += months[month]
    else:
        count += int(day)
if rounds >= 1:
    count += months[month - 1] - int(line.split("-")[2])
else:
    count += int(day) - int(line.split("-")[2])
start_day = days[days.index(weekday) - (count % 7)]
if count // 7 > 0:
    temp = count // 7
    error = 0
    for i in range(temp):
        try:
            with open(f".\\weeks\\{i + 1}.week.cfg", "r", encoding="utf-8") as file:
                line = file.readlines()
        except FileNotFoundError:
            error += 1
    if error == 1:    
        os.system(f"ren toDo.cfg {count // 7}.week.cfg & move {count // 7}.week.cfg weeks & ren toDo.cfg.next toDo.cfg")
    elif error >= 2:
        clear()
        input("Weeks missing...")
        sys.exit()
end = ""
while end.lower() != "q":
    clear()
    end = input("\t\tMENU\t\t\n\n|1| -> |Show all weeks|\n|2| -> |Show top 10 tasks|\n|3| -> |Search for specific task|\n|4| -> |Today's tasks|\n|5| -> |Edit planned tasks|\n|6| -> |Edit template|\n|q| -> |Quit|\n$~ ")
    msg = []
    sum = []
    num = []
    if count // 7 >= 1:
        for i in range(count // 7):
            count_tasks = 0
            try:
                with open(f".\\weeks\\{i + 1}.week.cfg", "r", encoding="utf-8") as file:
                    linos = file.readlines()
                    for lino in linos:
                        try:
                            main = lino.split(";")[1].split(",")
                            for contents in main:
                                try:
                                    if contents.split(":")[1].strip().lower() == "done":
                                        count_tasks += 1
                                        if contents.split(":")[0].strip().lower() not in sum:
                                            sum.append(contents.split(":")[0].strip().lower())
                                            num.append(1)
                                        else:
                                            num[sum.index(contents.split(":")[0].strip().lower())] += 1
                                except IndexError:
                                    pass
                        except IndexError:
                            pass
                msg.append(f"{i + 1}. Week consists of {count_tasks} done tasks")
            except FileNotFoundError:
                msg = ["Some weeks are missing..."]
                break
                    
    i = 0
    if "1" == end:
        clear()
        if count // 7 == 0:
            print("No data...")
        else:
            for ms in msg:
                print(ms)
        input()
        clear()
    msg = []
    for content in sum:
        msg.append(f"{content} -> {num[sum.index(content)]}")
    save = num
    num.sort(reverse=True)
    done = []
    if "2" == end:
        clear()
        if count // 7 == 0:
            print("No data...")
        else:
            print("10 popular tasks:")
        for i in range(10):
            for message in msg:
                if message.split("-> ")[1] == str(num[i]) and message not in done:
                    print(f"{i + 1}: {message}")
                    done.append(message)
        input()
        clear()
    if "3" == end:
        clear()
        if count // 7 == 0:
            print("No data...")
        else:
            find = input("Search for tasks:")
            text = list(find.lower())
            found = 0
            for message in msg:
                cor = 0
                saved = message
                right = 0
                bad = False
                message = message.split(" ->")[0].lower()
                temp = list(find)
                for lttr in list(message):
                    if lttr.lower() in temp:
                        temp.pop(temp.index(lttr.lower()))
                        cor += 1
                    try:
                        if lttr.lower() == text[list(message).index(lttr)].lower() and bad == False:
                            right += 1
                        else:
                            bad = True
                    except IndexError:
                        bad = True
                if right >= len(find) * 0.5 and cor >= len(find) * 0.5 or cor >= len(find) * 0.8 and right >= 2:
                    print(f"{message} -> {saved.split("-> ")[1]}")
                    found += 1
            if found == 0:
                print("Nothing corresponds to your search")
        input()
        clear()
    if "4" == end:
        while True:
            now = datetime.now()
            hour = now.hour
            minute = now.minute
            day = days[now.weekday()]
            listos = []
            clear()
            try:
                with open("toDo.cfg", "r", encoding="utf-8") as file:
                    linos = file.readlines()
                    print(f"{" "* ((len("|Enter number of done task to mark/unmark it as completed|") - len(f"day: {day}")) // 2)}day: {day}\n{" "* ((len("|Enter number of done task to mark/unmark it as completed|") - len(f"hour: {hour}")) // 2)}hour: {hour}\n{"=" * (len("|Enter number of done task to mark/unmark it as completed|"))}\n|Enter number of done task to mark/unmark it as completed|\n|Enter q to quit|\n{"=" * (len("|Enter number of done task to mark/unmark it as completed|"))}")
                    for line in linos:
                        line = line.strip()
                        day = line.split(";")[0]
                        if int(day) == now.weekday() + 1:
                            saved = int(day)
                            tasks = line.split(";")[1].split(",")
                            printed = False
                            for task in tasks:
                                if task == "":
                                    break
                                listos.append(f"{task},")
                                try:
                                    one = task.split(":")[0]
                                    two = task.split(":")[1]
                                    if two.lower() == "done":
                                        two = "✓"
                                    else:
                                        two = "✘"
                                    print(f"{tasks.index(task) + 1}.{one} {two}") 
                                    printed = True
                                except IndexError:
                                    print(f"{tasks.index(task) + 1}.{task} ✘")  
                                    printed = True
                            if printed == False:
                                clear()
                                with open("template.cfg", "r", encoding="utf-8") as file:
                                    lines = file.readlines()
                                    try:
                                        line = lines[0]
                                    except IndexError:
                                        line = ""
                                if line != "":
                                    q1 = input("No plan for today, do you want to apply your template?(y/n)\n$~ ")
                                    if q1.lower() == "y":
                                        with open("toDo.cfg", "r", encoding="utf-8") as file:
                                            lines = file.readlines()
                                            lines[now.weekday()] = f"{now.weekday()+ 1};{line.strip()}\n"
                                        with open("toDo.cfg", "w", encoding="utf-8") as file:
                                            file.writelines(lines)
                                        continue
                                else:
                                    input("No plan for today nor template created...")
                                    break
            except FileNotFoundError:
                sys.exit()
            if printed == True:
                ok = input()
                if ok.lower() == "q":
                    break
                try:
                    if int(ok.lower().split(".")[0]) <= len(tasks) and int(ok.lower().split(".")[0]) > 0:
                        try:
                            try:
                                if listos[int(ok) - 1].split(":")[1] == "done,":
                                    listos[int(ok) - 1] = f"{listos[int(ok) - 1].split(",")[0].split(":")[0]},"
                                else:
                                    listos[int(ok) - 1] = f"{listos[int(ok) - 1].split(",")[0]}:done,"
                            except IndexError:
                                listos[int(ok) - 1] = f"{listos[int(ok) - 1].split(",")[0]}:done,"
                            lino = "".join(listos)
                            lino = f"{saved};{lino}\n"
                            linos[saved - 1] = lino
                            with open("toDo.cfg", "w", encoding="utf-8") as file:
                                file.writelines(linos)
                        except IndexError:
                            input("Index Error")
                except ValueError:
                    pass
    if end == "6":
        temp = ""
        while temp.lower() != "q":
            clear()
            print(f"Enter task name(If task is already in -> task is deleted, else the task is created)\n   |q to quit|")
            try:
                with open("template.cfg", "r", encoding="utf-8") as file:
                    line = file.readlines()
            except FileNotFoundError:
                with open("template.cfg", "w", encoding="utf-8") as file:
                    file.write("")
                    line = []
            if line != []:
                for task in line[0].split(","):
                    if task != "":
                        print(f"{line[0].split(",").index(task) + 1}. {task}")
            temp = input("$~ ")
            if temp.lower() != "q":
                temp_list = []
                deleted = False
                if line != []:
                    temp_list = line[0].split(",")
                    for task in temp_list:
                        if task.lower() == temp.lower():
                            temp_list.pop(temp_list.index(task))
                            deleted = True
                main_list = []
                for task in temp_list:
                    if task != "," and task != "" and task != " ":
                        main_list.append(f"{task},")
                if deleted == False:
                    main_list.append(f"{temp},")
                with open("template.cfg", "w", encoding="utf-8") as file:
                    file.write("".join(main_list))


            

