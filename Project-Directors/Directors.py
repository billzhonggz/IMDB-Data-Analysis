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
# Extract columns
df1 = df[['Director', 'Title', 'Revenue (Millions)']]
# List all directors.
directorList = df1.groupby('Director')['Revenue (Millions)'].agg(['sum', 'count'])
print(directorList)
# Sorting by revenue, list the first five data.
firstFive = directorList.sort_values('sum', ascending=False).head()
print(firstFive)