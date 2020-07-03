from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import re
import sqlite3

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Movies')

cur.execute('''
CREATE TABLE IF NOT EXISTS Movies(
    id INTEGER PRIMARY KEY,
    release_date VARCHAR(16),
    movie_name VARCHAR(64),
    production_budget VARCHAR(16),
    domestic_gross VARCHAR(16),
    worldwide_gross VARCHAR(16)
)''')

data_listed = 100
count = 0
dataset_source_url = 'https://www.the-numbers.com/movie/budgets/all'

first_time = True

while True:
    if first_time is True:
        source_url = dataset_source_url
        first_time = False
    else:
        if data_listed <= 100:
            break

        temp = count + 1
        next_page = str(temp)
        source_url = dataset_source_url + "/" + next_page

    print("Extracting data from:", source_url)

    page = Request(source_url, headers={'User-Agent': 'Mozilla/5.0'})
    raw = urlopen(page).read()
    html = raw.decode()

    soup = BeautifulSoup(html, "html.parser")
    tags = soup('tr')
    data_listed = len(tags)

    first_iteration = True

    # Extracting data and inserting to database
    for tag in tags:
        money = list()

        if first_iteration is True:
            first_iteration = False
            continue

        for x in tag.contents:
            if x != '\n':
                string_tag = str(x)

                rd = re.findall('>([A-Z].+, .+[0-9])<', string_tag)
                mn = re.findall('ummary">([A-Z].+)</a', string_tag)
                doller = re.findall('(\\$[0-9].*)</td', string_tag)

                if len(rd) > 0:
                    release_data = rd[0]
                if len(mn) > 0:
                    movie_name = mn[0]
                if len(doller) > 0:
                    money.append(doller[0])

        production_budget = money[0]
        domestic_gross = money[1]
        worldwide_gross = money[2]

        cur.execute('''
        INSERT OR IGNORE INTO Movies(release_date, movie_name, production_budget, domestic_gross, worldwide_gross)
        VALUES(?, ?, ?, ?, ?)
        ''', (release_data, movie_name, production_budget, domestic_gross, worldwide_gross, ))

        count = count + 1
    conn.commit()

cur.close()

# Use DB Browser for SQLite to view 'data.sqlite' file
print("Data Scraping complete. Use any SQLite file viewer to open 'data.sqlite' file.")
print("Total number of retrieved data:", count)
print("Next run 'transform.py' to refine dataset and convert to csv file for applying Linear Regression")
