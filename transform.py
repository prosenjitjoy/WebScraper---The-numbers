from pandas import DataFrame
import sqlite3

try:
    conn = sqlite3.connect('data.sqlite')
    cur = conn.cursor()
    cur.execute('''
    SELECT production_budget, worldwide_gross
    FROM Movies
    ''')
except:
    print("Database Connection Error")
    print("Please run 'crawler.py' first to generate 'data.sqlite'")
    print("Then run this file to generate 'data.csv' file")
    quit()

production_budget = list()
worldwide_gross = list()

count = 0

for row in cur:
    pb = row[0]
    wg = row[1]

    pb = pb.replace(',', "")[1:]
    wg = wg.replace(',', "")[1:]

    if wg != "0":
        production_budget.append(pb)
        worldwide_gross.append(wg)

data = DataFrame({'production_budget': production_budget,
                  'worldwide_gross': worldwide_gross})
data.to_csv('data.csv', index=False, encoding='utf-8')

cur.close()

print("Data cleanup and csv file generated successfully")
print("Next run 'regression.ipynb' to view Linear Regression inside jupyter notebook")
