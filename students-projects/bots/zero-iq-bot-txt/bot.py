import random

DICT = {}


username = ''
FILENAME= './dictionary.txt'
SEPARATOR = '|'
CURRENT_LANGUAGE = 'english'

INTRO_WORDS = ['hello', 'hallo']
EXIT_WORDS = ['bye', 'tschuess']
LANGUAGES = ['english', 'german']

is_waiting_for_name = False
is_leaving = False


def add_question_to_dict(language, question, answer):
    if language not in DICT:
        DICT[language] = {}
    if question not in DICT[language]:
        DICT[language][question] = [answer]
    else:
        DICT[language][question].append(answer)


def fill_dict(filename):
    f = open(filename, 'r')
    for line in f:
        data = line.split(SEPARATOR)
        language = data[0].lower().rstrip()
        question = data[1].lower().rstrip()
        for i in range(2, len(data)):
            answer = data[i].rstrip()
            add_question_to_dict(language, question, answer)


def get_answer(question):
    if question in DICT[CURRENT_LANGUAGE]:
        return random.choice(DICT[CURRENT_LANGUAGE][question]).format(username)
    else:
        return 'do not understand'


fill_dict(FILENAME)

while not is_leaving:
    user_input = raw_input('->').lower().rstrip()

    if is_waiting_for_name:
        username = user_input
        user_input = 'name'
        is_waiting_for_name = False
    else:
        if user_input in INTRO_WORDS:
            is_waiting_for_name = True
        elif user_input in LANGUAGES:
            CURRENT_LANGUAGE = user_input
        elif user_input in EXIT_WORDS:
            is_leaving = True

    print(get_answer(user_input))
