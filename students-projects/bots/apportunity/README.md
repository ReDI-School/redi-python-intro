# Apportunity bot (the project is not 100% completed - see limitations)

## Description
Command-line bot which provides the list of known (predefined in csv file) opportunities based on user's input.\
The interaction with the bot follows the scenario:

1. The bot says "hi" and asks about user's name
2. Then it greets the user by their name
3. The bot asks the user to select one of the topics of interest from the list
4. The user chooses one topic
5. The Bot shows the user possible locations of opportunities for that topic
6. The user selects the location of interest
7. The bot shows existing opportunities of the given topic at the given location and asks if the user want's to change 
the topic of interest
8. If the user answers "Yes", conversation continues from the step 3., otherwise the bot tells the user "Goodbye" 
 
## Usage

Run the script bot.py with a path to a csv file with opportunities as an argument:
```bash
python3 bot.py opportunities.csv
```

## Limitations
* The bot doesn't support yet the location selection (the conversation continues only if oportunities are available only 
in one location)
* The bot doesn't handle the end of conversation but just finishes after showing the oportunity (or facing a 
non-implemented branch)