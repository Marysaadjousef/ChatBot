import json
import random
from difflib import get_close_matches


def load_intents_file(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def find_the_best_match (user_question : str, questions:list[str]) -> str or None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, intents: dict) -> str or None:
    for intent in intents["intents"]:
        if question in intent["patterns"]:
            return random.choice(intent["responses"])


def chatbot():
    inten: dict = load_intents_file('intents.json')

    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            break
        best_match: str or None = find_the_best_match(user_input,
                                                      [i for intent in inten["intents"] for i in intent["patterns"]])
        if best_match:
            answer: str = get_answer_for_question(best_match, inten)
            print(f'Bot: {answer}')
        else:
            print(f'Bot: what do you mean?')

            
if __name__ == '__main__':
    chatbot()
