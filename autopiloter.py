# Autopiloter
from datetime import date

print("Welcome")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
today = str(days[date.today().weekday()])
print("Today is: " + today)

print("Here is your baseline TODO list:")

monday_tasks = '''
    \u2022 Lifting
    \u2022 Running
    \u2022 Coding 1
    \u2022 Grocery Shopping
    \u2022 Wash Car
    \u2022 [ACTIVITY] Pool and Water Slides
    \u2022 Music
    \u2022 Cleaning: Kitchen, living room, bathroom, wipe desk
    \u2022 Art
        \u25CB 2D
        \u25CB 3D
    \u2022 Reading
    \u2022 Writing
    \u2022 Coding 2
    \u2022 Engineering
    \u2022 Visualization
    \u2022 Internet
    \u2022 Gaming
    \u2022 Game Development
        \u25CB Physics Programming
    \u2022 Career
    \u2022 Trello/Notion
    \u2022 Wash Bottles
    \u2022 Prep gym clothes
    \u2022 Prep regular clothes
    \u2022 Stretches and TV
'''


tuesday_tasks = '''
    \u2022 Lifting
    \u2022 Running
    \u2022 Coding 1
    \u2022 Music
    \u2022 Cleaning: Kitchen, living room, bedroom, wipe desk
    \u2022[EVENT] Writing Group 318
    \u2022 Art
        \u25CB 2D
        \u25CB 3D
    \u2022 Reading
    \u2022 Writing
    \u2022 Coding 2
    \u2022 Engineering
    \u2022 Visualization
    \u2022 Internet
    \u2022 Gaming
    \u2022 Game Development
        \u25CB Physics Programming
    \u2022 Career
    \u2022 Trello/Notion
    \u2022 Wash Bottles
    \u2022 Prep gym clothes
    \u2022 Stretches and TV
    '''

wednesday_tasks = '''
    \u2022 Lifting
    \u2022 Running
    \u2022 Coding 1
    \u2022 Music
    \u2022 Cleaning: Kitchen, living room, fridge, wipe desk
    \u2022 Art
        \u25CB  2D
        \u25CB  3D
    \u2022 Reading
    \u2022 Writing
    \u2022 Coding 2
    \u2022 Engineering
    \u2022 Visualization
    \u2022 Internet
    \u2022 Gaming
    \u2022 Game Development
        \u25CB Physics Programming
    \u2022 Career
    \u2022 Trello/Notion
    \u2022 Wash Bottles
    \u2022 Stretches and TV
    \u2022 Prep gym clothes
    \u2022 Band
'''

thursday_tasks = '''
    \u2022 Lifting
    \u2022 Running
    \u2022 Coding 1
    \u2022 Music
    \u2022 Cleaning: Kitchen, living room, deck, wipe desk
    \u2022 Art
        \u25CB 2D
        \u25CB 3D
    \u2022 Reading
    \u2022 Writing
    \u2022 Coding 2
    \u2022 Engineering
    \u2022 Visualization
    \u2022 Internet
    \u2022 Gaming
    \u2022 Game Development
        \u25CB Physics Programming
    \u2022 Career
    \u2022 Trello/Notion
    \u2022 Wash Bottles
    \u2022 Stretches and TV
    \u2022 Prep gym clothes
    \u2022 Theme Park Activity
'''

no_tasks_found = '''
    No tasks found yet!
'''

# don't forget writing group 321 on fri/sat
if today == "Monday":
    print(monday_tasks)
elif today == "Tuesday":
    print(tuesday_tasks)
elif today == "Wednesday":
    print(wednesday_tasks)
elif today == "Thursday":
    print(thursday_tasks)
else:
    print(no_tasks_found)

print("If 2-minute rule is complete, make a check on your calendar!")
print("If all tasks are completed to an adequate depth, put a star on top of the check!")
