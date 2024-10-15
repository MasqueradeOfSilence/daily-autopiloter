# -*- coding: utf-8 -*-
# Autopiloter
from datetime import date

print("Welcome")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
today = str(days[date.today().weekday()])
print("Today is: " + today)

monday_tasks = '''
    • Lifting
    • Running
    • Coding 1
    • Grocery Shopping
    • Wash Car
    • [ACTIVITY] Pool and Water Slides
    • Music
    • Cleaning: Kitchen, living room, bathroom, wipe desk
    • Art
        ○ 2D
        ○ 3D
    • Reading
    • Writing
    • Coding 2
    • Engineering
    • Visualization
    • Internet
    • Gaming
    • Game Development
    • Career
    • Trello/Notion
    • Wash Bottles
    • Prep gym clothes
    • Prep regular clothes
    • Stretches and TV
'''

tuesday_tasks = '''
    • Lifting
    • Running
    • Coding 1
    • Music
    • Cleaning: Kitchen, living room, bedroom, wipe desk
    • [EVENT] Writing Group 318
    • Art
        ○ 2D
        ○ 3D
    • Reading
    • Writing
    • Coding 2
    • Engineering
    • Visualization
    • Internet
    • Gaming
    • Game Development
    • Career
    • Trello/Notion
    • Wash Bottles
    • Prep gym clothes
    • Stretches and TV
'''

no_tasks_found = '''
    No tasks found yet!
'''

# don't forget writing group 321 on fri/sat
if today == "Monday":
    print(monday_tasks)
elif today == "Tuesday":
    print(tuesday_tasks)
else:
    print(no_tasks_found)
