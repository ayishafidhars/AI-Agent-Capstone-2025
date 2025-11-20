# main.py

from agents.safety_agent import SafetyAgent
from agents.productivity_agent import ProductivityAgent

def main():
    print("Welcome to your AI Personal Assistant!\n")
    
    safety_agent = SafetyAgent()
    productivity_agent = ProductivityAgent()

    while True:
        print("\nWhat do you want to do?")
        print("1. Safety / Emergency Help")
        print("2. Productivity / Study Assistance")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            message = input("\nDescribe your situation or threat: ")
            if safety_agent.is_danger(message):
                print("\n⚠️ Danger detected!")
                location = input("Enter your location (optional): ")
                sos = safety_agent.generate_sos(location)
                print(sos)
                print("\nImmediate Safety Instructions:")
                for instr in safety_agent.safety_instructions():
                    print(f"- {instr}")
            else:
                print("No immediate danger detected. Stay alert!")
        
        elif choice == "2":
            print("\nProductivity Options:")
            print("a. Add Task")
            print("b. View Tasks")
            print("c. Motivation Quote")
            option = input("Choose an option (a/b/c): ")
            if option.lower() == "a":
                task = input("Enter your task: ")
                deadline = input("Enter deadline (YYYY-MM-DD): ")
                print(productivity_agent.add_task(task, deadline))
            elif option.lower() == "b":
                tasks = productivity_agent.get_tasks()
                if tasks:
                    print("\nYour Tasks:")
                    for t in tasks:
                        print(f"- {t}")
                else:
                    print("No tasks found.")
            elif option.lower() == "c":
                print(productivity_agent.motivation_message())
            else:
                print("Invalid option.")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
