# Imports:
import json
from googlesearch import search
from colorama import init, Fore
from os import system, path
from datetime import datetime as dt
from time import sleep
from time import strftime as sf
from random import randint
import platform
import sqlite3
# ==============================================================================================
# Type of platform:
tp = platform.uname().system

# Cleaning the terminal by their platform:
if tp == 'Windows':

	# Cleaning the terminal on windows:
	system('cls')

else:

	# Cleaning the terminal on linux:
	system('clear')
# ==============================================================================================
# Initialize colorama:
init(autoreset=True)
# ==============================================================================================
# Get today date:
date = dt.today().strftime('%Y-%m-%d')

# date = '2023-10-03'  # uncomment this if you want to test and see the result

# List of all questions and google dorks:
list_of_questions = []
# ==============================================================================================
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
# ==============================================================================================
# Check if backup.json exists or not:
if path.exists('backup.json'):

	# Get the time and defrence it:
	with open('backup.json') as f:
		
		# json -> python:
		text = json.load(f)
		
		# Get the value of the "time" key:
		last_time = text["time"]

		# Get the current time: 
		now_time = sf("%H:%M")

		# Convert it to a type that can subtract them:
		last_time2 = dt.strptime(last_time, "%H:%M")
		now_time2 = dt.strptime(now_time, "%H:%M")
		
		# Subtract 2 times:
		delta = now_time2 - last_time2
		sec = delta.total_seconds()
		
		# Get the hour part:
		result_time = int(sec / (60 * 60))

		# Get the date:
		date_json = text['date']

		# Check if today's date and json's date is diffrent:
		if date_json != date:

			# Open backup.json to make changes:
			with open('backup.json', 'w') as ff:

				# Our new dictionary that we want to convert it to json:
				dict_t = {'date': date, 'time': last_time, 'stored-links': {}, 'stored-links-update': {}}

				# python -> json:
				json.dump(dict_t, ff, indent=4)

else:
	
	# Go create it and write the basic text in it:
	with open('backup.json', 'w') as f:
		
		# Get the current time: 
		now_time = sf("%H:%M")
		
		# Dictionary of basic info:
		dict1 = {'date': date, 'time': now_time, 'stored-links': {}, 'stored-links-update': {}}
		
		# python -> json:
		json.dump(dict1, f, indent=4)

	# Result time:
	result_time = 1
# ==============================================================================================
# Chceck if 1 hour passed:
if result_time >= 1:
	
	# Local data:
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
			
			# Add to data:
			l_data.update({title_s: url_s})

	# Read information:
	with open('backup.json') as f:
		
		# json -> python:
		data = json.load(f)

	# Update information in backup.json:
	with open('backup.json', 'w') as f:

		# new data:
		data.update({"stored-links-update": l_data})

		# Get the current time: 
		now_time = sf("%H:%M")

		# Update the value of "time" key:
		data.update({"time": now_time})

		# python -> json:
		json.dump(data, f, indent=4)
# ==============================================================================================
# Show the old data and the new ones:
with open('backup.json') as f:

	# json -> python:
	data = json.load(f)

	# Get if there is any update:
	result_data = set(data["stored-links-update"].keys()) - set(data["stored-links"].keys())

	print('the old ones: ')

	# Counter:
	c = 1

	for i in data["stored-links"]:
		
		# Show the result as a hyper link text and colorized:
		print(f'{Fore.LIGHTGREEN_EX}[{c}] {Fore.WHITE}- {Fore.MAGENTA}\x1b]8;;{data["stored-links"][i]}\x1b\\{i}\x1b]8;;\x1b\\')

		# Add to the counter:
		c += 1

	# Set counter again:
	c = 1

	print('the new ones: ')

	# Local data:
	l_data = {}

	# # Get access to any key of "stored-links-update":
	for i in data["stored-links-update"]:
		
		# Check if the title is unice:
		if i in result_data:
		
			# Show the result as a hyper link text and colorized:
			print(f'{Fore.LIGHTGREEN_EX}[{c}] {Fore.WHITE}- {Fore.CYAN}\x1b]8;;{data["stored-links-update"][i]}\x1b\\{i}\x1b]8;;\x1b\\')
			
			# Add to the "l_data":
			l_data.update({i: data["stored-links-update"][i]})
			
			# Add to the counter
			c += 1
	
	# Connect to the database:
	con = sqlite3.connect('links.db')

	# Create the cursor:
	c = con.cursor()

	# Get the year:
	td = date[:4]
	
	# Create table with the name of the year:
	c.execute(f'CREATE TABLE IF NOT EXISTS "{td}" (title , link , date)')

	# Get access to the each item of the dictionary:
	for i in l_data:

		# Insert the data into a reletive table, one by one:
		c.execute(f'INSERT INTO "{td}" VALUES (:title, :link, :date)'
			, {'title': i, 'link': l_data[i], 'date': date})
		
		# Make changes:
		con.commit()

# ==============================================================================================
# Moving all the links in "stored-links-update" to "stored-links"
with open('backup.json', 'w') as f:

	# Add anything in "stored-links-update" to the end of the "stored-links":
	new = data["stored-links"].update(l_data)
	
	# Make "stored-links-update" empty:
	data.update({"stored-links-update": {}})

	# python -> json:
	json.dump(data, f, indent=4)
# ==============================================================================================
## print("\x1b]8;;link\x1b\\text\x1b]8;;\x1b\\")

