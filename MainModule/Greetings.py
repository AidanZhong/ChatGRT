import random

with open('../Data/corpus/greetings.data', 'r', encoding='utf-8') as f:
    greetings = f.readlines()
    greetings = [greeting.strip() for greeting in greetings]


def greeting(name):
    random_greeting = random.choice(greetings).replace("[Name]", name)
    print(random_greeting + ' What can I do for you?')
