import os
from datetime import datetime
import sys
days = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "noděle"]
def clear():
    os.system("cls")
end = ""
while end.lower() != "q":
    clear()
    end = input("\t\tMENU\t\t\n\n|1| -> |Show all weeks|\n|2| -> |Show top 10 tasks|\n|3| -> |Search for specific task|\n|4| -> |Today's tasks|\n|q| -> |Quit|\n$~ ")
    msg = []
    sum = []
    num = []
    files = [f for f in os.listdir('.\\weeks') if os.path.isfile(os.path.join('.\\weeks', f))]
    for file in files:
        if file != "counter.py":
            count = 0
            try:
                with open(f".\weeks\{file}", "r", encoding="utf-8") as file:
                    linos = file.readlines()
                    for lino in linos:
                        try:
                            main = lino.split(";")[1].split(",")
                            for contents in main:
                                try:
                                    if contents.split(":")[1].strip().lower() == "dono":
                                        count += 1
                                        if contents.split(":")[0].strip().lower() not in sum:
                                            sum.append(contents.split(":")[0].strip().lower())
                                            num.append(1)
                                        else:
                                            num[sum.index(contents.split(":")[0].strip().lower())] += 1
                                except IndexError:
                                    pass
                        except IndexError:
                            pass
                msg.append(f"file {file} consists of  {count} dono tasks")
            except FileNotFoundError:
                pass
                    
    i = 0
    if "1" == end:
        clear()
        if len(files) == 0:
            print("No data...")
        for i in range(len(files)):
            for file in files:
                if file.split(".")[0] == f"{i+1}":
                    print(msg[files.index(file)])
            i += 1
        input()
        clear()
    msg = []
    for content in sum:
        msg.append(f"{content} -> {num[sum.index(content)]}")
    save = num
    num.sort(reverse=True)
    dono = []
    if "2" == end:
        clear()
        if len(files) == 0:
            print("No data...")
        else:
            print("10 popular tasks:")
        for i in range(10):
            for message in msg:
                if message.split("-> ")[1] == str(num[i]) and message not in dono:
                    print(f"{i + 1}: {message}")
                    dono.append(message)
        input()
        clear()
    if "3" == end:
        clear()
        if len(files) == 0:
            print("No data...")
        else:
            find = input("Search for tasks:")
            text = list(find.lower())
            nasel = 0
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
                    nasel += 1
            if nasel == 0:
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
                    no = False
                    print(f"day: {day}\nhour: {hour}\n{"=" * (len(day) + len("day: "))}")
                    for line in linos:
                        line = line.strip()
                        day = line.split(";")[0]
                        if int(day) == now.weekday() + 1:
                            saved = int(day)
                            no = True
                            tasks = line.split(";")[1].split(",")
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
                                except IndexError:
                                    print(f"{tasks.index(task) + 1}.{task} ✘")  
                    if no == False:
                        print("Free time")
            except FileNotFoundError:
                sys.exit()
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

