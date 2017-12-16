# IMDb movie data analysis - Directors
# by Junru (Bill) Zhong, 1430003045
# 1. List all directors.
# 2. Get the total revenues each directors got.
# 3. Rank all directors by revenues got each film in average.
# 4. List information of directed film(s) of the top-5 directors.
# 5. Estimate the revenues of their next film by some algorithms.

import pandas as pd

# Read csv.
df = pd.read_csv('../Dataset/IMDB-Movie-Data.csv')

# List all directors.
directorList = df.groupby('Director')['Revenue (Millions)'].agg(['sum', 'count']).reset_index()
# Delete invalid data
directorList = directorList.dropna()
# Get average revenue of each director.
directorList['avg'] = directorList['sum'] / directorList['count']
print(directorList)
# Sorting by revenue, list the first five data.
firstFive = directorList.sort_values('avg', ascending=False).head()
print(firstFive)
# The first five directors are:
#             Director      sum  count      avg
# 261    James Cameron   760.51      1  760.510
# 114  Colin Trevorrow   652.18      1  652.180
# 341      Joss Whedon  1082.27      2  541.135
# 377      Lee Unkrich   414.98      1  414.980
# 208        Gary Ross   408.00      1  408.000

# Searching their works.
directorNames = firstFive['Director']
for directorName in directorNames:
    for index, row in df.iterrows():
        if row['Director'] == directorName:
            print(row['Director'] + ', ' + row['Genre'] + ', ' + row['Title'])
# Result
# James Cameron, Action,Adventure,Fantasy, Avatar
# Colin Trevorrow, Action,Adventure,Sci-Fi, Jurassic World
# Joss Whedon, Action,Sci-Fi, The Avengers
# Joss Whedon, Action,Adventure,Sci-Fi, Avengers: Age of Ultron
# Lee Unkrich, Animation,Adventure,Comedy, Toy Story 3
# Gary Ross, Adventure,Sci-Fi,Thriller, The Hunger Games
# Gary Ross, Action,Biography,Drama, Free State of Jones