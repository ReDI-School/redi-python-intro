import yaml
import random
import datetime
import string


class zero_iq_bot:
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
        if 'answers' in self.bot_dictionary[self.language][question]:
            print(random.choice(self.bot_dictionary[self.language][question]['answers']).format(self.username))

    def act(self, question):
        if 'action' in self.bot_dictionary[self.language][question]:
            action = self.bot_dictionary[self.language][question]['action']
            if action == 'get_name':
                self.username = ' ' + input()
            elif action == 'print_time':
                print(datetime.datetime.now())
            elif action == 'exit':
                exit()

    def react(self, question):
        if 'reactions' in self.bot_dictionary[self.language][question]:
            print(random.choice(self.bot_dictionary[self.language][question]['reactions']).format(self.username))

    def process_user_input(self, user_input):
        user_input = user_input.lower().rstrip()
        for char in string.punctuation:
            user_input = user_input.replace(char, "")

        for question in self.bot_dictionary[self.language]:
            if (question == user_input or
               ('synonyms' in self.bot_dictionary[self.language][question] and
                 user_input in self.bot_dictionary[self.language][question]['synonyms'])):

                self.answer(question)
                self.act(question)
                self.react(question)


def main():
    bot = zero_iq_bot()
    while True:
        user_input = input('->')
        bot.process_user_input(user_input)


if __name__ == '__main__':
    main()
