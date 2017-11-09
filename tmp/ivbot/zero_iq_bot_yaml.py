import yaml
import random
import datetime

DICT = {}
USERNAME = ''
LANGUAGE = 'english'


def load_dict_from_file(filename):
    with open(filename, 'r') as dictionary_file:
        return yaml.load(dictionary_file)


def action_get_name():
    global USERNAME
    USERNAME = input()


def action_print_time():
    print(datetime.datetime.now())


def action_exit():
    exit()


def answer(question):
    if 'answers' in DICT[LANGUAGE][question]:
        print(random.choice(DICT[LANGUAGE][question]['answers']).format(USERNAME))


def act(question):
    if 'action' in DICT[LANGUAGE][question]:
        function = "action_{0}()".format(DICT[LANGUAGE][question]['action'])
        eval(function)


def react(question):
    if 'reactions' in DICT[LANGUAGE][question]:
        print(random.choice(DICT[LANGUAGE][question]['reactions']).format(USERNAME))


DICT = load_dict_from_file('dictionary.yaml')
print(DICT)
while True:
    user_input = input('->').lower().rstrip()
    if user_input in DICT[LANGUAGE]:
        answer(user_input)
        act(user_input)
        react(user_input)


