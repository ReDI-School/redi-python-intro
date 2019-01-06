# Ideas for the projects that weren't implemented (yet)

## Maze game

### One Street Game
    
Write a program that takes from the user 'Right' or 'Left'. The program should print accordingly
an X showing where you are on a 10 block street.

Initially the program Prints:
``` 
X . . . . . . . . .
```

If the user enters 'Right', the program prints:
``` 
. X . . . . . . . .
```
If the user enters another 'Right', the program prints:
``` 
. . X . . . . . . .
```
If the user enters 'Left', the program prints:
``` 
. X . . . . . . . .
```
 
### A Walk in the park
    
Write a program that takes from the user 'Left', 'Right', 'Up', 'Down'. The program should print 
the map of the park (3*3 Grid) and X showing the player's location.\
Initially player is situated in the top left corner.

Initially the program Prints:
``` 
X . .
. . .
. . . 
```
If the user enters 'Right', the program prints:
``` 
. X .
. . .
. . . 
```
If the user enters  'Down', the program prints:
``` 
. . .
. X .
. . . 
```
If the user enters 'Left', the program prints:
``` 
. . .
X . .
. . .  
```
If the user enters 'Left', the program prints:
``` 
. . .
. . .
. . . 
```
'You are no longer in the park! Good bye!'

### A Walk in a maze

Write a program that takes from the user 'Left', 'Right', 'Up', 'Down'. The program should print 
the map of the maze (4*4 Grid) and X showing the player's location.\
The 4X4 Grid has blocking walls, that the player can't walk through. The position of these walls the program should take 
as input.\
Initially player is situated in the top left corner. 

Initially the program prints (assuming the user set the walls on positions 1,1 and 2,2):
``` 
X . . .
. W . .
. . W .
. . . .
```

If the user enters 'Right', the program prints:
``` 
. X . .
. W . .
. . W .
. . . .
```

If the user enters  'Down', the program prints:
``` 
. X . .
. W . .
. . W .
. . . .
Wall!
```

If the user enters 'Right', the program prints:
``` 
. . X .
. W . .
. . W .
. . . .
```
If the user enters 'Down', the program prints:
``` 
. . . .
. W X .
. . W .
. . . .
```

### A Walk in a maze 2.0


Modification of the previous program:
* user can enter the desired size of the maze
* maze can be populated by the walls automatically (random choice)
* user can enter the starting position
* user can modify the generated maze    

  







    

     
    
    
    
    
  
    
    
   