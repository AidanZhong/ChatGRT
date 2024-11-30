import random

greetings = [
    "Hi, [Name]!",
    "Hey, [Name]!",
    "Hello, [Name]!",
    "What's up, [Name]?",
    "Yo, [Name]!",
    "Good to see you, [Name]!",
    "Hey there, [Name]!",
    "Hiya, [Name]!",
    "How’s it going, [Name]?",
    "Long time no see, [Name]!",
    "Nice to meet you, [Name].",
    "Pleased to see you, [Name].",
    "Hey [Name], so great to see you!",
    "Hello there, [Name]! How have you been?",
    "Hey [Name], it’s been a while!",
    "Hi [Name]! How’s everything?",
    "Oh my gosh, [Name]! It’s so good to see you!",
    "Hey, [Name], how are you doing today?",
    "Hello, [Name]! How have you been?",
    "Hey [Name], everything good with you?",
    "Hi [Name], how’s your day going?",
    "Hello, [Name]. How’s life treating you?",
    "[Name]! Fancy meeting you here!",
    "Look who it is—[Name]!",
    "Hey [Name], long time no see!",
    "There you are, [Name]!",
    "[Name], it’s been too long!"
]


def greeting(name):
    random_greeting = random.choice(greetings).replace("[Name]", name)
    print(random_greeting + ' What can I do for you?')
