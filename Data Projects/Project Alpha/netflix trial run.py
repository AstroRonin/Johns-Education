import pandas as pd
import matplotlib.pyplot as plt

#path to csv file
netflix_list = pd.read_csv('E:/Coding/Self Learning/Johns-Education/Data Projects/Project Alpha/titles_update.csv')

netflix_list['date_added'] = pd.to_datetime(netflix_list['date_added'])

netflix_list['year_added'] = netflix_list['date_added'].dt.year

netflix_list['month_added'] = netflix_list['date_added'].dt.month

netflix_list = netflix_list.dropna(subset=['type'])

#count of shows and movies added each year
count_by_type_year = netflix_list.groupby(['type', 'year_added']).size().unstack(fill_value=0)

#plot of data
count_by_type_year.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Number of Movies vs. TV Shows added to Netflix (2008 - 2021)')
plt.xlabel('Year')
plt.ylabel('Number of titles added')
plt.legend(title='Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
