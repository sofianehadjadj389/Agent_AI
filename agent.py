import datetime

class Agent:
    def __init__(self, name, memory):
        self.name = name
        self.memory = memory
        self.knowledge = {
            "bonjour": "Bonjour Sofiane,comment puis-je t’aider ?",
            "comment vas tu": "ca va et toi !",
            "merci": "Avec plaisir !",
            "ton nom": f"Je m'appelle {self.name}.",
            "qui t'as créé": "Sofiane Ayoudj.",
            "tu fais quoi": "Je suis un agent. Je peux enregistrer notre discution et répondre à des questions.",
            "aide": "Tu peux me poser une question ou consulter ma mémoire.",
            "comment tu vas": "Je vais bien, merci et toi ?",
            "je vais bien": "super,",
            "bye": "Au revoir ! Reviens quand tu veux."
        }

    def ask(self, question):
        question_lower = question.lower().strip()

        # ajoute de calcule et l'heure
        if "calcule" in question_lower or "combien" in question_lower:
            try:
                expr = question_lower.replace("calcule", "").replace("combien", "").strip()
                result = eval(expr)
                answer = f"Le résultat est {result}"
            except:
                answer = "Je n’ai pas compris ton calcul. Essaie quelque chose comme 'calcule 5 + 8'."
        elif "heure" in question_lower:
            now = datetime.datetime.now().strftime("%H:%M")
            answer = f"Il est {now}."
        elif "date" in question_lower:
            today = datetime.datetime.now().strftime("%d/%m/%Y")
            answer = f"Aujourd'hui, on est le {today}."
        elif question_lower in self.knowledge:
            answer = self.knowledge[question_lower]
        else:
            answer = f"Désolé, je ne sais pas répondre à ça encore."

        self.memory.save_interaction(question, answer)
        return answer
