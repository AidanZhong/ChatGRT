import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import CommonUtils, IntentMatching, Greetings


def identity_matching():
    try:
        user_name = CommonUtils.DatabaseUtils.get_last_visit_user()
        print(f'Hi, is that still {user_name}?')
        res = input()
        if IntentMatching.yes_or_no(res):
            Greetings.greeting(user_name)
            CommonUtils.DatabaseUtils.user_is_using(user_name)
        else:
            print('So, what is your name then?')
            res = input()
            name = get_name_from_response(res)
            if not name:
                name = res
            CommonUtils.DatabaseUtils.user_is_using(name)
            Greetings.greeting(name)
    except Exception as e:
        # do not have a user yet
        print('Hi, what is your name?')
        res = input()
        name = get_name_from_response(res)
        if not name:
            name = res
        CommonUtils.DatabaseUtils.user_is_using(name)
        Greetings.greeting(name)


def get_name_from_response(res):
    """
    get the name from a response
    :param res: response message
    :return: name
    """
    with open('./corpus/Name_saying', 'r') as f:
        patterns = f.readlines()

    pattern_with_placeholder = [pattern.replace("XXX", "(.*)").strip() for pattern in patterns]
    vectorizer = TfidfVectorizer()
    pattern_vectors = vectorizer.fit_transform(patterns)
    res_vector = vectorizer.transform([res])
    similarities = cosine_similarity(res_vector, pattern_vectors)
    best_pattern = pattern_with_placeholder[similarities.argmax()]

    match = re.search(best_pattern, res, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    else:
        return None
