<h1>Google Search Automation for Medium Posts </h1>
<h3>Get the latests articles about your favorite Topic in <a href="https://medium.com"> Medium </a> with only 1 python script ! </h3>
<h5> &#9679; by Pyteach ( Mohammad javad Azizi ) </h5>
<br>
<br>
<h1>  Question ❓</h1>
<br>
<h2> How this script works ? </h2>
<br>

1. **Get Today's Date**:
   - Retrieves today’s date to filter articles published after this date.

2. **Read Questions from a File**:
   - Reads questions from a text file called `questions.txt` and prepares search queries for each question formatted for Google search.

3. **Check Time Since Last Run**:
   - Reads the last run time from a `backup.json` file to determine if at least one hour has passed since the last search. If an hour has not passed, it retrieves previously saved articles instead of searching again.

4. **Perform Google Search**:
   - If one hour has passed, the script searches for each question on Medium using Google. It pauses for a random time (1 to 10 seconds) between searches to avoid being flagged as a bot.

5. **Display Results**:
   - For each search result, it extracts the title and URL, displays them in a formatted way, and adds them to a data dictionary.

6. **Update Backup Data**:
   - After retrieving new articles, the script updates the `backup.json` file with the latest articles and the current time.

7. **Display Old Data**:
    - If less than an hour has passed since the last run, the script displays the previously saved articles from the `backup.json` file.

<br>

<h1>How to use this ?</h1>

first of all, you need to open the terminal ( or cmd ) in project main directory , then you should run the command below to install all of the libraries that we need:
```
pip install -r requirements.txt
```
after you installed all the libraries , you have to specify what topics you want to get from medium in the question.txt file:
<br>
for example :
```question.txt
sql injection bug
different type of security attacks
```
> [!IMPORTANT]
> You have to seprate each line with an enter

after that you should just run this command in project directory:
```
python main.py
```

> [!NOTE]
> This script only shows the first 100 results and only today's posts

> [!WARNING]
> if you try to run the script less than 1 hour, it just show previous result
