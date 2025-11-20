# main.py
# AI Personal Safety & Productivity Agent
# Created by Ayisha for AI Agent Capstone 2025

import datetime


def greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good Morning 🌤️"
    elif hour < 17:
        return "Good Afternoon ☀️"
    else:
        return "Good Evening 🌙"


def show_menu():
    print("\nWhat do you want help with today?")
    print("1. Safety Tips")
    print("2. Study Motivation")
    print("3. Health Reminder")
    print("4. Daily Plan")
    print("5. Exit")


def safety_tips():
    print("\n🛡️ SAFETY MODE")
    print("- Always share your live location with a trusted person.")
    print("- Avoid isolated paths at night.")
    print("- Keep emergency contacts ready.")
    print("- Your safety matters more than anything.")


def study_motivation():
    print("\n📚 STUDY MODE")
    print("You are stronger than your excuses.")
    print("Study for future YOU.")
    print("25 minutes focus. 5 minutes break.")
    print("Repeat. You’ve got this!")


def health_reminder():
    print("\n💧 HEALTH MODE")
    print("- Drink a glass of water now.")
    print("- Stretch your body for 2 minutes.")
    print("- Take a deep breath 10 times.")
    print("- Eat something healthy today.")


def daily_plan():
    print("\n🗓️ DAILY PLAN MODE")
    tasks = []
    while True:
        task = input("Add a task (or type 'done'): ")
        if task.lower() == "done":
            break
        tasks.append(task)

    print("\n✅ Your plan for today:")
    for t in tasks:
        print("- " + t)


def main():
    print("=" * 50)
    print(greeting())
    print("Welcome to your AI Personal Companion")
    print("=" * 50)

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            safety_tips()
        elif choice == "2":
            study_motivation()
        elif choice == "3":
            health_reminder()
        elif choice == "4":
            daily_plan()
        elif choice == "5":
            print("\nGoodbye! Stay safe and keep growing 🌷")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
