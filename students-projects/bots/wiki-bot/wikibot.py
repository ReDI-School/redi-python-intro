import yaml
import random
import datetime
import string
import wikipedia
import textwrap

WIKI_LANGUAGES = {'english': 'en', 'русский': 'ru', 'deutsch': 'de'}

class wiki_bot:
    bot_dictionary = {}
    username = ''
    language = ''

    def __init__(self, dictionary_filename='./dictionary.yaml', language='english'):
        self.bot_dictionary = self.load_dict_from_file(dictionary_filename)
        self.username = ''
        self.language = language

    @staticmethod
    def load_dict_from_file(filename):
        with open(filename, 'r') as dictionary_file:
            return yaml.load(dictionary_file)

    def answer(self, question):
        if 'answers' in self.bot_dictionary[question]:
            print(random.choice(self.bot_dictionary[question]['answers'][self.language]).format(self.username))

    def act(self, question):
        if 'action' in self.bot_dictionary[question]:
            action = self.bot_dictionary[question]['action']
            if action == 'get_name':
                self.username = ' ' + input()
            elif action == 'search_wiki':
                print(textwrap.fill(wikipedia.summary(input(), sentences=3), width=80))
            elif action == 'print_time':
                print(datetime.datetime.now())
            elif 'language' in action:
                self.language = action.replace('language ', '')
                wikipedia.set_lang(WIKI_LANGUAGES[self.language])
            elif action == 'exit':
                exit()

    def react( self, question):
        if 'reactions' in self.bot_dictionary[question]:
            print(random.choice(self.bot_dictionary[question]['reactions'][self.language]).format(self.username))

    def process_user_input(self, user_input):
        user_input = user_input.lower().rstrip()
        for char in string.punctuation:
            user_input = user_input.replace(char, "")

        for question in self.bot_dictionary:
            if (question == user_input or
               ('synonyms' in self.bot_dictionary[question] and
                 self.language in self.bot_dictionary[question]['synonyms'] and
                 user_input in self.bot_dictionary[question]['synonyms'][self.language])):

                self.answer(question)
                self.act(question)
                self.react(question)


def main():
    bot = wiki_bot('./dictionarys.yaml')
    while True:
        user_input = input('->')
        bot.process_user_input(user_input)


if __name__ == '__main__':
    main()
