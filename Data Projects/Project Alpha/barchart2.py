import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

netflix_list = pd.read_csv('E:/Coding/Self Learning/Johns-Education/Data Projects/Project Alpha/titles_update.csv')

netflix_list['date_added'] = pd.to_datetime(netflix_list['date_added'], errors='coerce')

movies_df = netflix_list[netflix_list['type'] == 'Movie']
tv_shows_df = netflix_list[netflix_list['type'] == 'TV Show']   

movies_count_by_year = movies_df.groupby(movies_df['date_added'].dt.year).size()
tv_shows_count_by_year = tv_shows_df.groupby(tv_shows_df['date_added'].dt.year).size()

plt.figure(figsize=(12, 8)) 

bar_width = 0.35
years = sorted(set(movies_count_by_year.index) | set(tv_shows_count_by_year.index))

max_count = max(len(movies_count_by_year), len(tv_shows_count_by_year))
years_position = np.arange(max_count)

plt.barh(years_position - bar_width / 2, movies_count_by_year.reindex(years).fillna(0).values, color='blue', label='Movies')
plt.barh(years_position + bar_width / 2, tv_shows_count_by_year.reindex(years).fillna(0).values, color='red', label='TV Shows')

plt.yticks(years_position, years) 
plt.xticks(np.arange(0, max(max(movies_count_by_year), max(tv_shows_count_by_year)) + 1, 50)) 
plt.xlabel('Number of Titles')
plt.ylabel('Year')
plt.title('Number of Movies vs TV Shows added to Netflix (2008 - 2021)')
plt.legend()
plt.tight_layout()  
plt.show()
