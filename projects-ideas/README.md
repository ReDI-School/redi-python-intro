**Apportunity - FB chatbot**





Echo Bot:
   
   an annoying bot that repeats everything you say until you say 'I am leaving'



 Zero IQ Bot (German & Enlgish)

    Given a set of template question-answers. If someone asks a question, bot will respond 
    with corresponding answer, if he types something else, it simply says 
    "Sorry, I don't have an answer to this, try asking another question"
    A user at any point can switch between english and german when user types 'speak english'/
    'speak german'


Apportunity - Bot 0.0

    1. Bot says hi and asks about your name
    2. it then greets the user by name
    3. Asks him which of the below topics he like?
    4. User chooses one topic
    5. Bot shows the user the opportunities for each topic
    6. User asks about more information for a specific opportunity
    7. Bot tells him details about it and a contact email for more info
    8. Bot asks if he would like to ask about another topic
    9. if Yes, Go back to step 5, if no, Bot tells the user Goodbye 


 

Phase 2

Create a class Topic:

Each topic has attributes
    
    1. title
    2. picture url
    3. sub-topics
 
Create a class called Opportunity
Each opportunity has attributes

    1. title
    2. contact email
    3. date
    4. time
    5. rating
    6. topic

    
Create a class user:
Each user has attributes:

    1. id
    2. name
    3. date of birth
    4. nationality
    5. visa status
    6. email
    7. interests
    8. bookmarked opportunities
    
    

We are able to do the following actions

For opportunity:

    1. rate an opportunity
    2. reschedule
    
For a user:

    1. add an interest 
    2. remove an interest
    3. bookmark an opportunity
    4. get the closest upcoming opportunitiy
    5. get the most recent past opportunity

For a topic:

    1. Add an opportunity to a topic
    2. get sub topics
    3. get upcoming opportunities for topic



**Maze**


One Street Game
    
    Write a program that takes from the user 'Right' or 'Left'. The program should print accordingly
    an X showing where you are on a 10 block street.
    --------------------------------
    Initially Program Prints:
    X . . . . . . . . .
    If the user enters 'Right', program prints:
    . X . . . . . . . .
    If the user enters another 'Right', program prints:
    . . X . . . . . . .
    If the user enters 'Left', program prints:
    . X . . . . . . . .
 
A Walk in the park
    
    Write a program that takes from the user 'Left', 'Right', 'Up', 'Down'. The program should print accordingly
    and X showing where you are on a 3X3 Grid. Initially player is in top left corner
    ---------------------------
    Initially Program Prints:
    X . .
    . . .
    . . . 
    If the user enters 'Right', program prints:
    . X .
    . . .
    . . . 
    If the user enters  'Down', program prints:
    . . .
    . X .
    . . . 
    If the user enters 'Left', program prints:
    . . .
    X . .
    . . .  
    If the user enters 'Left', program prints:
    . . .
    . . .
    . . . 
    'You are no longer in the park! Good bye!'

Wall
    
    Write a program that takes from the user 'Left', 'Right', 'Up', 'Down'. The program should print accordingly
    and X showing where you are on a 4X4 Grid. The 4X4 Grid has blocking walls , that you can't walk through it
    The position of these walls you take as input.
    Initially player is in top left corner
    ---------------------------
    Initially Program Prints:
    X . . .
    . W . .
    . . W .
    . . . .
    
    If the user enters 'Right', program prints:
    . X . .
    . W . .
    . . W .
    . . . .
    
    
    If the user enters  'Down', program prints:
    . X . .
    . W . .
    . . W .
    . . . .
    'Wall!'
    
    If the user enters 'Right', program prints:
    . . X .
    . W . .
    . . W .
    . . . .
    If the user enters 'Down', program prints:
    . . . .
    . W X .
    . . W .
    . . . .


Maze 0.0

    Write a program that takes size of maze if it is 5, the maze is 5 X 5 , and a list of wall positions, and play maze!
    
Create a class called Board:
 
    - Board Object is initialized given two parameters: size, is_random
    - if is_random is true, block positions are generated
    - if is_random is false, program asks user to enter wall positions

You can do the following actions on board:
    1. add wall
    2. add player
    3. remove player
    4. check empty cell
    
  







    

     
    
    
    
    
  
    
    
   