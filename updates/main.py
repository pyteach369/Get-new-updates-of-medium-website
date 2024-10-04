# Imports:
import json
from googlesearch import search
from colorama import init, Fore, Back
from os import system, path
from datetime import datetime as dt
from time import sleep
from time import strftime as sf
from random import randint

# Cleaning the terminal:
system('cls')

# Initialize colorama:
init(autoreset=True)

# Counter:
c = 1

# Get today date:
date = dt.today().strftime('%Y-%m-%d')
# date = '2024-09-28'  # uncomment this if you want to test and see the result

# List of all questions and google dorks:
list_of_questions = []

# Reading questions file:
with open('questions.txt') as f:
	
	# Get all lines:
	questions = f.readlines()
	
	# Config and append it to the main list:
	for i in questions:
	
		# Replace \n with nothing:
		i = i.replace('\n', '')

		# Append the google dork into list_of_questions:
		list_of_questions.append(f'site:medium.com "{i}" after:{date}')

# Get the time and defrence it:
with open('backup.json') as f:
	
	# json -> python:
	text = json.load(f)
	
	# get the value of the "time" key:
	last_time = text["time"]

	# get the current time: 
	now_time = sf("%H:%M")

	# convert it to a type that can subtract them:
	last_time = dt.strptime(last_time, "%H:%M")
	now_time = dt.strptime(now_time, "%H:%M")
	
	# subtract 2 times:
	delta = now_time - last_time
	sec = delta.total_seconds()
	
	# get the hour part:
	result_time = int(sec / (60 * 60))

# Chceck if 1 hour passed:
if result_time >= 1:
	
	l_data = {}

	# Search all questions one by one:
	for i in list_of_questions:

		# Choose a random number between 1 to 10:
		rn = randint(1,10)
		
		# Sleep program in "rn" seconds:
		sleep(rn)

		# Search the question and get all the result links with title:
		result_list = list(search(i, num_results=100, advanced=True, sleep_interval=5))
		
		# Show the links one by one:
		for j in result_list:

			# Url and title:
			url_s = j.url
			title_s = j.title
			
			# Show the result as a hyper link text and colorized:
			print(f'{Fore.LIGHTGREEN_EX}[{c}] {Fore.WHITE}- {Fore.CYAN}\x1b]8;;{url_s}\x1b\\{title_s}\x1b]8;;\x1b\\')

			# Add to data:
			l_data.update({title_s: url_s})

			# Add to our counter:
			c += 1

	# Read information:
	with open('backup.json') as f:
		
		# json -> python:
		data = json.load(f)

	# Update information in backup.json:
	with open('backup.json', 'w') as f:

		# new data:
		data.update({"stored-links": l_data})

		# Get the current time: 
		now_time = sf("%H:%M")

		# Update the value of "time" key:
		data.update({"time": now_time})

		# python -> json:
		json.dump(data, f, indent=4)

else:
	
	# Show the old data:
	with open('backup.json') as f:

		# json -> python:
		data = json.load(f)

		for i in data["stored-links"]:
			
			# Show the result as a hyper link text and colorized:
			print(f'{Fore.LIGHTGREEN_EX}[{c}] {Fore.WHITE}- {Fore.CYAN}\x1b]8;;{data["stored-links"][i]}\x1b\\{i}\x1b]8;;\x1b\\')

			# Add to the counter:
			c += 1

## print("\x1b]8;;link\x1b\\text\x1b]8;;\x1b\\")

