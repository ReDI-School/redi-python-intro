__author__ = "Ilya Vladimirskiy"
__email__ = "bkmy43@googlemail.com"

import random
import os
import time

MAZE_WIDTH = 20
MAZE_HEIGHT = 20
MAX_STEPS = 5000
PAUSE_BETWEEN_STEPS = 0.05


class Maze:
    cur_x = 0
    cur_y = 0
    entrance = (0, 0)

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.exit = (height, width)
        self.walls = [[False for i in range(width)] for j in range(height)]
        self.visited = [[False for i in range(width)] for j in range(height)]
        self.visited_count = [[0 for i in range(width)] for j in range(height)]

    def cur_position(self):
        return self.cur_y, self.cur_x

    def display(self):
        symbols = {"CUR_POSITION": u'ME', "VISITED": u'\u2591\u2591', "NOT_VISITED": '  ', "WALL": u'\u2588\u2588',
                   "H_BOUND": u'\u2501\u2501', "V_BOUND": u'\u2503',
                   "UP_LEFT": u'\u250F', "UP_RIGHT": u'\u2513', "BOTTOM_LEFT": u'\u2517', "BOTTOM_RIGHT": u'\u251B'}

        print("Maze size: {}*{}\nEntrance: {}, Exit: {}".format(self.height, self.width, self.entrance, self.exit))

        str = symbols.get("UP_LEFT")
        for j in range(self.width):
            if (0, j) != self.entrance and (0, j) != self.exit:
                str = str + symbols.get("H_BOUND")
            else:
                str = str + '  '
        print(str + symbols.get("UP_RIGHT"))

        for i in range(self.height):
            if (i, 0) != self.entrance and (i, 0) != self.exit:
                str = symbols.get("V_BOUND")
            else:
                str = ' '

            for j in range(self.width):
                if (i, j) == self.cur_position():
                    str = str + symbols.get("CUR_POSITION")
                else:
                    if self.walls[i][j]:
                        str = str + symbols.get("WALL")
                    elif self.visited[i][j]:
                        str = str + symbols.get("VISITED")
                    else:
                        str = str + symbols.get("NOT_VISITED")

            if (i, j) != self.entrance and (i, j) != self.exit:
                str = str + symbols.get("V_BOUND")

            print(str)

        str = symbols.get("BOTTOM_LEFT")
        for j in range(self.width):
            if (self.height - 1, j) != self.entrance and (self.height - 1, j) != self.exit:
                str = str + symbols.get("H_BOUND")
            else:
                str = str + '  '
        print(str + symbols.get("BOTTOM_RIGHT"))

    def clear(self):
        self.cur_y = self.entrance[0]
        self.cur_x = self.entrance[1]
        self.visited = [[False for i in range(self.width)] for j in range(self.height)]
        self.visited_count = [[0 for i in range(self.width)] for j in range(self.height)]

    def randomize(self, walls_density=0.25):
        self.entrance = self.get_random_position_on_maze_boundary()
        self.exit = self.get_random_position_on_maze_boundary()
        self.cur_y = self.entrance[0]
        self.cur_x = self.entrance[1]

        for i in range(self.height):
            for j in range(self.width):
                if random.random() < walls_density and (i, j) != self.entrance and (i, j) != self.exit:
                    self.walls[i][j] = True

    def get_random_position_on_maze_boundary(self):
        boundaries = ['UP', 'LEFT', 'BOTTOM', 'RIGHT']

        wall = random.choice(boundaries)

        if wall == 'UP':
            return (0, random.choice(range(self.width)))
        elif wall == 'BOTTOM':
            return (self.height - 1, random.choice(range(self.width)))
        elif wall == 'LEFT':
            return (random.choice(range(self.height)), 0)
        elif wall == 'RIGHT':
            return (random.choice(range(self.height)), self.width - 1)

    def move(self, direction):
        if direction == 'UP':
            if self.cur_y > 0 and not self.walls[self.cur_y - 1][self.cur_x]:
                self.cur_y = self.cur_y - 1
            else:
                return False
        elif direction == 'DOWN':
            if self.cur_y < self.height - 1 and not self.walls[self.cur_y + 1][self.cur_x]:
                self.cur_y = self.cur_y + 1
            else:
                return False
        elif direction == 'LEFT':
            if self.cur_x > 0 and not self.walls[self.cur_y][self.cur_x - 1]:
                self.cur_x = self.cur_x - 1
            else:
                return False
        elif direction == 'RIGHT':
            if self.cur_x < self.width - 1 and not self.walls[self.cur_y][self.cur_x + 1]:
                self.cur_x = self.cur_x + 1
            else:
                return False

        self.visited[self.cur_y][self.cur_x] = True
        self.visited_count[self.cur_y][self.cur_x] += 1

        return True

    def chaotic_run(self):
        for i in range(MAX_STEPS):
            time.sleep(PAUSE_BETWEEN_STEPS)
            os.system('clear')
            self.move(random.choice(('UP', 'DOWN', 'LEFT', 'RIGHT')))
            self.display()
            if self.cur_position() == self.exit:
                print("Successfully reached exit. {} steps were needed".format(i + 1))
                return True
            print("This is CHAOTIC RUN\nTrying to get out of this maze... {} steps done".format(i + 1))

        print("Maximum of {} steps reached, exit not found...".format(i + 1))
        return False

    def smart_run(self):
        for i in range(MAX_STEPS):
            time.sleep(PAUSE_BETWEEN_STEPS)
            os.system('clear')
            self.move(self.get_best_move())
            self.display()
            if self.cur_position() == self.exit:
                print("Sucessfully reached exit. {} steps were needed".format(i + 1))
                return True
            print("This is SMART RUN\nTrying to get out of this maze... {} steps done".format(i + 1))
        print("Maximum of {} steps reached, exit not found...".format(i + 1))
        return False

    def get_best_move(self):
        moves = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        options = {}
        new_position = (self.cur_y, self.cur_x)

        for move in moves:
            if move == 'UP':
                new_position = (self.cur_y - 1, self.cur_x)
            elif move == 'DOWN':
                new_position = (self.cur_y + 1, self.cur_x)
            elif move == 'LEFT':
                new_position = (self.cur_y, self.cur_x - 1)
            elif move == 'RIGHT':
                new_position = (self.cur_y, self.cur_x + 1)

            if new_position[0] >= 0 \
                    and new_position[0] < self.height \
                    and new_position[1] >= 0 \
                    and new_position[1] < self.width \
                    and not self.walls[new_position[0]][new_position[1]]:
                options[move] = self.get_distance(self.exit, new_position) \
                                * (self.visited_count[new_position[0]][new_position[1]] + 1)

        return min(options, key=options.get)

    def get_distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


os.environ['TERM'] = 'xterm'

print('Maze generated:')

m1 = Maze(MAZE_WIDTH, MAZE_HEIGHT)
m1.randomize(0.25)
m1.display()

while True:
    command = input('Press:\ns - for smart run\nc - for chaotic run\nother key - to exit\n')
    if command == 's':
        m1.smart_run()
    elif command == 'c':
        m1.chaotic_run()
    else:
        break
    command = input('Press:\nc - to generate a new maze and continue\nr - to continue with the same maze'
                    '\nother key - to exit\n')
    if command == 'c':
        print('Maze generated:')

        m1 = Maze(MAZE_WIDTH, MAZE_HEIGHT)
        m1.randomize(0.25)
        m1.display()
    elif command == 'r':
        m1.clear()
        m1.display()
    else:
        break



