# agents/productivity_agent.py

"""
ProductivityAgent
-----------------
This agent helps with:
- Study scheduling
- Task reminders
- Focus & motivation
- Logging productivity in memory
"""

import datetime

class ProductivityAgent:
    def __init__(self, memory_file="memory.txt"):
        self.memory_file = memory_file

    def add_task(self, task: str, deadline: str):
        """
        Add a task with deadline
        """
        entry = f"Task: {task} | Deadline: {deadline} | Added: {datetime.datetime.now()}"
        self.save_to_memory(entry)
        return f"Task '{task}' added with deadline {deadline}"

    def get_tasks(self):
        """
        Retrieve all tasks from memory
        """
        try:
            with open(self.memory_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            return []

        tasks = [line.strip() for line in lines if "Task:" in line]
        return tasks

    def motivation_message(self):
        """
        Return a motivational quote
        """
        quotes = [
            "Focus on progress, not perfection!",
            "Small steps every day lead to big results!",
            "Stay consistent and you will succeed!",
            "Your effort today builds your success tomorrow."
        ]
        import random
        msg = random.choice(quotes)
        self.save_to_memory(f"Motivation given: {msg}")
        return msg

    def save_to_memory(self, content: str):
        """
        Save events into memory file
        """
        with open(self.memory_file, "a", encoding="utf-8") as f:
            f.write("\n--- PRODUCTIVITY LOG ---\n")
            f.write(str(datetime.datetime.now()) + "\n")
            f.write(content + "\n")
