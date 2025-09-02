import os
import time
import calendar
from datetime import datetime

NOTES_FILE = "notes.txt"
TODO_FILE = "todo.txt"
REMINDER_FILE = "reminders.txt"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to return to menu...")

def ascii_logo():
    return r"""
 _____ _____ ___ _____ 
'########::'########:::::'###::::
 ##.... ##: ##.... ##:::'## ##:::
 ##:::: ##: ##:::: ##::'##:. ##::
 ########:: ##:::: ##:'##:::. ##:
 ##.....::: ##:::: ##: #########:
 ##:::::::: ##:::: ##: ##.... ##:
 ##:::::::: ########:: ##:::: ##:
..:::::::::........:::..:::::..::"""

def show_clock():
    clear()
    now = datetime.now()
    print("⏰ CLOCK")
    print("--------")
    print("Current time:", now.strftime("%H:%M:%S"))
    print("Current date:", now.strftime("%Y-%m-%d"))
    pause()

def notes():
    clear()
    print("📝 NOTES")
    print("--------")
    print("1. View Notes")
    print("2. Add Note")
    print("3. Clear Notes")
    choice = input("Choose an option: ")

    if choice == "1":
        clear()
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r") as f:
                print(f.read())
        else:
            print("No notes yet.")
    elif choice == "2":
        note = input("Enter your note: ")
        with open(NOTES_FILE, "a") as f:
            f.write(note + "\n")
        print("Note added.")
    elif choice == "3":
        open(NOTES_FILE, "w").close()
        print("Notes cleared.")
    else:
        print("Invalid option.")
    pause()

def todo_list():
    clear()
    print("✅ TO-DO LIST")
    print("-------------")
    if not os.path.exists(TODO_FILE):
        open(TODO_FILE, "w").close()

    with open(TODO_FILE, "r") as f:
        tasks = [line.strip() for line in f]

    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

    print("\nA - Add R - Remove C - Clear Q - Back")
    choice = input("Choose an option: ").lower()

    if choice == "a":
        task = input("Enter new task: ")
        with open(TODO_FILE, "a") as f:
            f.write(task + "\n")
    elif choice == "r":
        try:
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(tasks):
                del tasks[index - 1]
                with open(TODO_FILE, "w") as f:
                    for t in tasks:
                        f.write(t + "\n")
                print("Task removed.")
            else:
                print("Invalid index.")
        except:
            print("Error: Invalid input.")
    elif choice == "c":
        open(TODO_FILE, "w").close()
        print("To-do list cleared.")
    pause()

def calendar_view():
    clear()
    year = datetime.now().year
    month = datetime.now().month

    while True:
        clear()
        print("📅 CALENDAR")
        print("------------")
        print(calendar.month(year, month))
        print("P - Previous N - Next Q - Back")
        cmd = input("Choice: ").lower()
        if cmd == "p":
            month -= 1
            if month < 1:
                month = 12
                year -= 1
        elif cmd == "n":
            month += 1
            if month > 12:
                month = 1
                year += 1
        elif cmd == "q":
            break

def reminders():
    while True:
        clear()
        print("🔔 REMINDERS")
        print("-------------")
        if not os.path.exists(REMINDER_FILE):
            open(REMINDER_FILE, "w").close()

        with open(REMINDER_FILE, "r") as f:
            lines = f.readlines()

        if lines:
            for idx, line in enumerate(lines, 1):
                print(f"{idx}. {line.strip()}")
        else:
            print("No reminders yet.")

        print("\nA - Add R - Remove C - Clear Q - Back")
        choice = input("Choose an option: ").lower()

        if choice == "a":
            text = input("Reminder text: ")
            time_str = input("Time (HH:MM 24hr): ")
            with open(REMINDER_FILE, "a") as f:
                f.write(f"{text} at {time_str}\n")
        elif choice == "r":
            try:
                index = int(input("Enter number to remove: "))
                if 1 <= index <= len(lines):
                    del lines[index - 1]
                    with open(REMINDER_FILE, "w") as f:
                        f.writelines(lines)
                    print("Reminder removed.")
                else:
                    print("Invalid index.")
            except:
                print("Invalid input.")
        elif choice == "c":
            open(REMINDER_FILE, "w").close()
            print("Reminders cleared.")
        elif choice == "q":
            break
        else:
            print("Invalid option.")
        pause()

def check_reminders():
    now_time = datetime.now().strftime("%H:%M")
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip().endswith(now_time):
                    print(f"\n🔔 REMINDER: {line.strip()} 🔔")
                    print("Press Enter to acknowledge.")
                    input()

def main():
    while True:
        clear()
        now = datetime.now()
        check_reminders()

        print(ascii_logo())
        print(f"Time: {now.strftime('%H:%M:%S')} Date: {now.strftime('%Y-%m-%d')}")
        print("=" * 40)
        print("1. Notes")
        print("2. To-Do List")
        print("3. Calendar")
        print("4. Clock")
        print("5. Reminders")
        print("6. Exit")
        print("=" * 40)
        choice = input("Select an option: ")

        if choice == "1":
            notes()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            calendar_view()
        elif choice == "4":
            show_clock()
        elif choice == "5":
            reminders()
        elif choice == "6":
            clear()
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
            time.sleep(1)

if __name__ == "__main__":
    main()
