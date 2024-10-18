# Autopiloter
# RUN: python3 autopiloter.py
from datetime import date

print("Welcome")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
today = str(days[date.today().weekday()])
print("Today is: " + today)

print("Here is your baseline TODO list:")

monday_tasks = '''
    \u2022 Lifting: Full body
    \u2022 Running: 6 miles
    \u2022 Coding 1: DSA, Kaggle, Cybersec
    \u2022 Grocery Shopping
    \u2022 Wash Car
    \u2022 [ACTIVITY] Pool and Water Slides
    \u2022 Music: Clarinet, Voice, Piano
    \u2022 Cleaning: Kitchen, living room, bathroom, wipe desk
    \u2022 Make breakfast and lunch for tomorrow, make dinner for tonight
    \u2022 Art
        \u25CB 2D
            \u25aa Warm-Ups: Browse art sites, Posemaniacs daily pose, 2 Quickposes poses, 1 hand, 1 foot, 1 face, 1 anime, 1 animal, Drawabox
            \u25aa Workout: Anime
            \u25aa 50% Rule
        \u25CB 3D
    \u2022 Reading
        \u25CB Novels
        \u25CB Webcomics
        \u25CB FF
        \u25CB NoSleep
        \u25CB Kindle
    \u2022 Writing
        \u25CB Morning pages
        \u25CB Novel WIP x285 words
        \u25CB Novel 2 WIP x143 words
        \u25CB FF
        \u25CB Poetry exercises
        \u25CB English review
    \u2022 Coding 2: Website, Embedded
    \u2022 Engineering: Math, EE/ME
    \u2022 Visualization
    \u2022 Internet
    \u2022 Gaming
    \u2022 Game Development
        \u25CB Physics Programming
    \u2022 Career
        \u25CB Job market evaluations
        \u25CB Freelancing (optional)
    \u2022 Trello/Notion
    \u2022 Wash Bottles
    \u2022 Prep gym clothes
    \u2022 Prep regular clothes
    \u2022 Stretches and TV
'''


tuesday_tasks = '''
    \u2022 Lifting: Push 
    \u2022 Running: 6 miles
    \u2022 Coding 1: DSA, Kaggle, Cybersec
    \u2022 Music: Clarinet, Voice, Piano
    \u2022 Cleaning: Kitchen, living room, bedroom, wipe desk
    \u2022[EVENT] Writing Group 318
    \u2022 Art
        \u25CB 2D
            \u25aa Warm-Ups: Browse art sites, Posemaniacs daily pose, 2 Quickposes poses, 1 hand, 1 foot, 1 face, 1 anime, 1 animal
            \u25aa Workout: Traditional drawing
            \u25aa 50% Rule
        \u25CB 3D
    \u2022 Reading
        \u25CB Novels
        \u25CB Webcomics
        \u25CB FF
        \u25CB NoSleep
        \u25CB Kindle
    \u2022 Writing
        \u25CB Morning pages
        \u25CB Novel WIP x285 words
        \u25CB Novel 2 WIP x143 words
        \u25CB FF
        \u25CB Poetry exercises
        \u25CB English review
    \u2022 Coding 2: Website, SWE
    \u2022 Engineering: Math, PLCs
    \u2022 Visualization
    \u2022 Internet
    \u2022 Gaming
    \u2022 Game Development
        \u25CB Physics Programming
    \u2022 Career
        \u25CB Job market evaluations
        \u25CB Freelancing (optional)
    \u2022 Trello/Notion
    \u2022 Wash Bottles
    \u2022 Prep gym clothes
    \u2022 Stretches and TV
    '''

wednesday_tasks = '''
    \u2022 Lifting: Legs
    \u2022 Running: 6 miles
    \u2022 Coding 1: DSA, Kaggle, Cybersec
    \u2022 Music: Clarinet, Voice, Piano
    \u2022 Cleaning: Kitchen, living room, fridge, wipe desk
    \u2022 Art
        \u25CB  2D
            \u25aa Warm-Ups: Browse art sites, Posemaniacs daily pose, 2 Quickposes poses, 1 hand, 1 foot, 1 face, 1 anime, 1 animal, Drawabox
            \u25aa Workout: Animals
            \u25aa 50% Rule
        \u25CB  3D
    \u2022 Reading
        \u25CB Novels
        \u25CB Webcomics
        \u25CB FF
        \u25CB NoSleep
        \u25CB Kindle
    \u2022 Writing
        \u25CB Morning pages
        \u25CB Novel WIP x285 words
        \u25CB Novel 2 WIP x143 words
        \u25CB FF
        \u25CB Poetry exercises
        \u25CB English review
    \u2022 Coding 2: Website, IT/Cyber
    \u2022 Engineering: Math, EE/ME
    \u2022 Visualization
    \u2022 Internet
    \u2022 Gaming
    \u2022 Game Development
        \u25CB Physics Programming
    \u2022 Career
        \u25CB Job market evaluations
        \u25CB Freelancing (optional)
    \u2022 Trello/Notion
    \u2022 Wash Bottles
    \u2022 Stretches and TV
    \u2022 Prep gym clothes
    \u2022 [EVENT] Band
'''

thursday_tasks = '''
    \u2022 Lifting: Pull day
    \u2022 Running: 6 miles
    \u2022 Coding 1: DSA, Kaggle, Cybersec
    \u2022 Music: Clarinet, Voice, Piano
    \u2022 Cleaning: Kitchen, living room, deck, wipe desk
    \u2022 Art
        \u25CB 2D
            \u25aa Warm-Ups: Browse art sites, Posemaniacs daily pose, 2 Quickposes poses, 1 hand, 1 foot, 1 face, 1 anime, 1 animal, Drawabox
            \u25aa Workout: Digital Painting
            \u25aa 50% Rule
        \u25CB 3D
    \u2022 Reading
        \u25CB Novels
        \u25CB Webcomics
        \u25CB FF
        \u25CB NoSleep
        \u25CB Kindle
    \u2022 Writing
        \u25CB Morning pages
        \u25CB Novel WIP x285 words
        \u25CB Novel 2 WIP x143 words
        \u25CB FF
        \u25CB Poetry exercises
        \u25CB English review
    \u2022 Coding 2: Website, Graphics
    \u2022 Engineering: Math, PLCs
    \u2022 Visualization
    \u2022 Internet
    \u2022 Gaming
    \u2022 Game Development
        \u25CB Physics Programming
    \u2022 Career
        \u25CB Job market evaluations
        \u25CB Freelancing (optional)
    \u2022 Trello/Notion
    \u2022 Wash Bottles
    \u2022 Stretches and TV
    \u2022 Prep gym clothes
    \u2022 Theme Park Activity
'''

friday_tasks = '''
    \u2022 Lifting: Abs
    \u2022 Running: 6 miles
    \u2022 Coding 1: DSA, Kaggle, Cybersec
    \u2022 Music: Clarinet, Voice, Piano
    \u2022 Cleaning: Kitchen, living room, PC, wipe desk
    \u2022 Throw in laundry needed for Saturday's long run
    \u2022 Art
        \u25CB 2D
            \u25aa Warm-Ups: Browse art sites, Posemaniacs daily pose, 2 Quickposes poses, 1 hand, 1 foot, 1 face, 1 anime, 1 animal, Drawabox
            \u25aa Workout: Free choice
            \u25aa 50% Rule
        \u25CB 3D
    \u2022 Reading
        \u25CB Novels
        \u25CB Webcomics
        \u25CB FF
        \u25CB NoSleep
        \u25CB Kindle
    \u2022 Writing
        \u25CB Morning pages
        \u25CB Novel WIP x285 words
        \u25CB Novel 2 WIP x143 words
        \u25CB FF
        \u25CB Poetry exercises
        \u25CB English review
    \u2022 Submit for BOTH writing groups 
    \u2022 Read for 321 writing group
    \u2022 Coding 2: Website, Free choice
    \u2022 Engineering: Math, theme park resort
    \u2022 Visualization
    \u2022 Internet
    \u2022 Gaming
        \u25CB Since it's Friday, leave at least an hour for this if you can!
    \u2022 Game Development
        \u25CB Physics Programming
    \u2022 Career
        \u25CB Job market evaluations
        \u25CB Freelancing (optional)
    \u2022 Trello/Notion
    \u2022 Wash Bottles
    \u2022 Stretches and TV
    \u2022 Prep gym clothes
    \u2022 [EVENT] Writing Group 321 (either today or Saturday)
'''

saturday_tasks = '''
    \u2022 Lifting: Full body / free choice
    \u2022 Running: 16-20 miles
    \u2022 Coding 1: DSA, Kaggle, Cybersec
    \u2022 Music: Clarinet, Voice, Piano
    \u2022 Cleaning: Wipe desk
    \u2022 Art
        \u25CB 2D
            \u25aa Warm-Ups: Browse art sites, Posemaniacs daily pose, 2 Quickposes poses, 1 hand, 1 foot, 1 face, 1 anime, 1 animal, Drawabox
            \u25aa Workout: Anime, traditional drawing, animals, digital painting
            \u25aa 50% Rule
            \u25CB Long-term projects: Evaluate progress
        \u25CB 3D
    \u2022 Reading
        \u25CB Novels
        \u25CB Webcomics
        \u25CB FF
        \u25CB NoSleep
        \u25CB Kindle
    \u2022 Writing
        \u25CB Morning pages
        \u25CB Novel WIP x285 words
        \u25CB Novel 2 WIP x143 words
        \u25CB FF
        \u25CB Poetry exercises
        \u25CB English review
    \u2022 Coding 2: Website, embedded, SWE, security, graphics
    \u2022 Engineering: Math, free choice
    \u2022 Visualization
    \u2022 Internet
    \u2022 Gaming
    \u2022 Game Development
        \u25CB Physics Programming
    \u2022 Career
        \u25CB Job market evaluations
        \u25CB Freelancing (optional)
    \u2022 Trello/Notion
    \u2022 Wash Bottles
    \u2022 Stretches and TV
    \u2022 Caturday (cat meme time)
    \u2022 Theme Park Activity
    \u2022 [EVENT] Writing Group 321 (if not done on Friday)
'''

sunday_tasks = '''
    \u2022 read lifting blogs / watch videos
    \u2022 Walking 1
    \u2022 Coding 1: DSA, Kaggle, Cybersec
    \u2022 Music: Clarinet, Voice, Piano
    \u2022 Cleaning: Hand-washed laundry, rest of laundry, laundry room
    \u2022 Piano Performance OR run-through
    \u2022 [EVENT] Choir 
    \u2022 Art
        \u25CB 2D
            \u25aa Warm-Ups: Browse art sites, Posemaniacs daily pose, 2 Quickposes poses, 1 hand, 1 foot, 1 face, 1 anime, 1 animal, Drawabox
            \u25aa Workout: Free choice
            \u25aa 50% Rule
        \u25CB 3D
    \u2022 Reading
        \u25CB Novels
        \u25CB Webcomics
        \u25CB FF
        \u25CB NoSleep
        \u25CB Kindle
    \u2022 Read for 318 writing group
    \u2022 Writing
        \u25CB Morning pages
        \u25CB Novel WIP x285 words
        \u25CB Novel 2 WIP x143 words
        \u25CB FF
        \u25CB Poetry exercises
        \u25CB English review
    \u2022 Coding 2: Website, free choice
    \u2022 Engineering: Math 
    \u2022 Visualization
    \u2022 Internet
    \u2022 Gaming
    \u2022 Game Development
        \u25CB Physics Programming
    \u2022 Career
        \u25CB Job market evaluations
        \u25CB Freelancing (optional)
    \u2022 Trello/Notion
    \u2022 Walking 2
    \u2022 Wash Bottles
    \u2022 Wash nightguard/retainer
    \u2022 Stretches and TV
    \u2022 Prep gym clothes
    \u2022 Call home
'''

no_tasks_found = '''
    No tasks found yet!
'''

if today == "Monday":
    print(monday_tasks)
elif today == "Tuesday":
    print(tuesday_tasks)
elif today == "Wednesday":
    print(wednesday_tasks)
elif today == "Thursday":
    print(thursday_tasks)
elif today == "Friday":
    print(friday_tasks)
elif today == "Saturday":
    print(saturday_tasks)
elif today == "Sunday":
    print(sunday_tasks)
else:
    print(no_tasks_found)

print("\n\nIf 2-minute rule is complete, make a check on your calendar!")
print("If you break past the 2-minute rule on all tasks and hit medium depth, put a moon on top of the check!")
print("If all tasks are completed fully, put a star on top of the moon and check!\n\n")
# TODO PyQt (?) layout and actual task completion
# TODO percentage in list of overarching tasks/projects
