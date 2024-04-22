import pandas as pd
import matplotlib.pyplot as plt

netflix_list = pd.read_csv('E:/Coding/Self Learning/Johns-Education/Data Projects/Project Alpha/titles_update.csv')

movies_df = netflix_list[netflix_list['type'] == 'Movie']
tv_shows_df = netflix_list[netflix_list['type'] == 'TV Show']   

movies_count_by_year = movies_df.groupby(movies_df['date_added'].dt.year).size()
tv_shows_count_by_year = tv_shows_df.groupby(tv_shows_df['date_added'].dt.year).size()

plt.figure(figsize=(10, 6))

plt.barh(movies_count_by_year.index, movies_count_by_year.values, color='blue', label='Movies')

plt.barh(tv_shows_count_by_year.index, tv_shows_count_by_year.values, color='red', label='TV Shows')

plt.xlabel('Number of Titles')
plt.ylabel('Year')
plt.title('Number of Movies vs TV Shows added to Netflix (2008 - 2021)')
plt.legend()
plt.show()