# Wiki bot

## Description
Simple command-line bot program with the list of predefined user commands and answers stored in .yaml file.\
The main function of the bot is to perform search in [Wikipedia](https://www.wikipedia.org/) by user's request.\
The bot also supports:
* addressing a user by their name
* understanding synonyms for user's commands
* providing one of several synonymous answers to the same question (chosen randomly for each question)
* three languages (English, Russian and German)

The bot can work in two modes: 
* local command-line application
* server application which can be controlled remotely 

## Requirements
### Both modes
[wikipedia](https://pypi.org/project/wikipedia/)
```bash
sudo pip3 install wikipedia
```

### Server mode 
[Flask](https://pypi.org/project/Flask/) 
```bash
sudo pip3 install Flask
```
[Flask-Script](https://pypi.org/project/Flask-Script/) 
```bash
sudo pip3 install Flask-Script
```
 
## Usage

### Both modes
The bot understands the following commands: 
* Greetings from the user (e.g. "Hello") 
* Commands to finish the conversation (e.g. "exit")
* Wikipedia search request (e.g. "search")
* Command to show the time (e.g. "time")
* User's reaction for the answer (e.g. "Thanks!")

the conversation can be started with a greeting word. The complete list of supported commands can be found in file 
./dictionary.yaml.

### Local command-line application
Run the script wikibot.py:
```bash
python3 wikibot.py
```

### Server application
Run the server:
```bash
python3 server.py runserver
```
By default the server listens to the incoming connections on the port 5000.\
You can send commands to the bot by adding them as values of a request parameter "user", e.g. with wget: 
```bash
wget 127.0.0.1:5000/?user=hello
```
or you can type the address with parameters in your browser address bar.\
The server doesn't send answers back but rather prints them in it's own terminal.

## Limitations
### Both modes 
The bot can't handle Wikipedia search results when there are more than one article in the results.
### Server application
The server doesn't send answers back but rather prints them in it's own terminal.