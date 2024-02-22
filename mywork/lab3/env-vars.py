#!/c/Users/hziegler/AppData/Local/Programs/Python/Python312/python

import os

sport = input('What is your favorite sport? ')
state = input('What state are you from? ')
high_school = input('What high school did you go to? ')

os.environ["SPORT"] = sport
os.environ["STATE"] = state
os.environ["HIGH_SCHOOL"] = high_school

print(os.getenv("SPORT"))
print(os.getenv("STATE"))
print(os.getenv("HIGH_SCHOOL"))
