import pandas as pd
from scraper import scraper_yellow_pages
from dataframe_script import process_dataframe
from loading_data import load_data_to_database


# Scraping the data using the function from scraper module
results = scraper_yellow_pages()

# creating a DataDrame from the dictionary returned by the scraper
df = pd.DataFrame.from_dict(results)

# cleaning and processing the data using the function from dataframe_script module
cleaned_df = process_dataframe(df)

# # loading the cleanded data into the PostgreSQL databse using the function from loading_data module
load_data_to_database(cleaned_df)
