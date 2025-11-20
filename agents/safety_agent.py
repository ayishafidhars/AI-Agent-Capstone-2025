# agents/safety_agent.py

"""
SafetyAgent
-----------
This agent is responsible for:
- Detecting dangerous situations
- Generating SOS messages
- Giving safety guidance
- Logging incidents to memory

This file is part of the AI-Agent-Capstone-2025 project
"""

import datetime


class SafetyAgent:
    def __init__(self, memory_file="memory.txt"):
        self.memory_file = memory_file

    def is_danger(self, message: str) -> bool:
        """
        Detects possible danger keywords in a user message
        """
        danger_words = [
            "followed", "scared", "danger", "help", "threat",
            "attack", "alone", "unsafe", "creep", "dark", "scream"
        ]

        message = message.lower()
        for word in danger_words:
            if word in message:
                return True
        return False

    def generate_sos(self, location="unknown"):
        """
        Creates an SOS message
        """
        sos_message = f"""
🚨 EMERGENCY ALERT 🚨

I am in danger and need immediate help!
Location: {location}
Time: {datetime.datetime.now()}

Please contact emergency services or reach me ASAP.
"""
        self.save_to_memory(sos_message)
        return sos_message

    def safety_instructions(self):
        """
        Gives immediate safety instructions
        """
        return [
            "Move to a public or crowded place immediately.",
            "Call emergency number or a trusted contact.",
            "Keep your phone battery and data on.",
            "Share live location with a trusted person.",
            "Avoid isolated areas and dark paths."
        ]

    def save_to_memory(self, content: str):
        """
        Saves events into memory file
        """
        with open(self.memory_file, "a", encoding="utf-8") as f:
            f.write("\n--- SAFETY LOG ---\n")
            f.write(str(datetime.datetime.now()) + "\n")
            f.write(content + "\n")
