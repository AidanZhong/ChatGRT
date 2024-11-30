import logging
import sys

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from IntentMatching import yes_or_no

logging.basicConfig(
    filename="HAI.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)

sys.path.append('./')


def process_with_user_said(user_said):
    """

    :param user_said: what the user said before intent matching
    :return: nothing
    """
    user_said = input('Yes, please feel free to ask!\n')
    data = pd.read_csv('./corpus/QandA.csv')
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(data['Question'])

    while True:
        query_vector = vectorizer.transform([user_said])
        similarities = cosine_similarity(query_vector, tfidf).flatten()

        best_match_index = similarities.argmax()

        best_match_question = data['Question'][best_match_index]
        best_match_answer = data['Answer'][best_match_index]
        logging.info(
            f"User input is {user_said}, the best match question is {best_match_question}, the best match answer is {best_match_answer}")

        print(f'Do you mean {best_match_question} ?')
        s = yes_or_no(input())
        if s:
            print(f'{best_match_answer}')
            continue_or_not = input('Would you like to continue to ask questions?')
            if not yes_or_no(continue_or_not):
                print('Thanks for using the Q&A session, what else can I do for you?')
                break
        else:
            print('Can you restate your question?')
        user_said = input()
