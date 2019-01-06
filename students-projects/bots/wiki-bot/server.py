import wikibot
from flask import Flask, request
from flask_script import Manager


app = Flask(__name__)

@app.route("/")
def run_wiki_bot():
    bot = wikibot.wiki_bot('./dictionary.yaml')
    while True:
        user_input = request.args.get('user')
        bot.process_user_input(user_input)


manager = Manager(app)

if __name__ == '__main__':
    manager.run()
