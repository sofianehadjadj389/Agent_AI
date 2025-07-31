
from agent import Agent
from memory import Memory

class Interface:
    def __init__(self):
        self.memory = Memory()
        self.agent = Agent("AIAgent", self.memory)

    def ask(self, question):
        if not question.strip():
            return "Merci d’écrire quelque chose."
        return self.agent.ask(question)
