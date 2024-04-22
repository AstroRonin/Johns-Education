import pandas as pd

netflix_list = pd.read_csv('E:/Coding/Self Learning/Johns-Education/Data Projects/Project Alpha/netflix_titles.csv')

netflix_list['date_added'] = pd.to_datetime(netflix_list['date_added'], errors='coerce')

netflix_list['date_added'] = netflix_list['date_added'].fillna(netflix_list['date_added'].astype(str))

netflix_list.to_csv('E:/Coding/Self Learning/Johns-Education/Data Projects/Project Alpha/titles_update.csv', index=False)