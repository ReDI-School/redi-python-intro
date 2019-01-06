# Zero IQ bot (yaml file-based)

## Description
Simple command-line bot program with the list of predefined user commands and answers stored in .yaml file.\
The bot supports addressing a user by their name, understanding synonyms for user's commands and providing 
one of several synonymous answers to the same question (chosen randomly for each question). 
   
## Usage
The bot understands the following commands: 
* Greetings from the user (e.g. "Hello") 
* Commands to finish the conversation (e.g. "exit")
* One question about registration process in Germany (e.g. "registration")
* Command to show the time (e.g. "time")
* User's reaction for the answer (e.g. "Thanks!")

the conversation can be started with a greeting word. The complete list of supported commands can be found in file 
./dictionary.yaml.