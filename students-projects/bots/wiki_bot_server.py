import wiki_bot
from flask import Flask, request
from flask_script import Manager


app = Flask(__name__)

@app.route("/")
def run_wiki_bot():
    bot = wiki_bot.wiki_bot('./wiki_dict.yaml')
    while True:
        user_input = request.args.get('user')
        bot.process_user_input(user_input)


manager = Manager(app)

if __name__ == '__main__':
    manager.run()
