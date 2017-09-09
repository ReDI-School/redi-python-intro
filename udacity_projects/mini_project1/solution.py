import time
import webbrowser

total_breaks = 3
break_count = 0

print('The program started at time '+ time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=g3VbTGxk4Sg&feature=youtu.be')
    break_count += 1