#import pandas library
import pandas as pd

#define the function that takes dataframe as input
def process_dataframe(df):

    # #set pandas display option to show all columns
    # pd.set_option("display.max_columns", None)

    #extract only the numerical rating from the "tripadvisor_rating" column using regular expressions
    df["tripadvisor_rating"] = df["tripadvisor_rating"].str.extract(r"(\d+\.\d+)")
    
    #remove new line character from "phone_number column"
    df["phone_number"] = df["phone_number"].str.replace("\n", "")
    
    #extract only numerical rating from the "yp_star_ratings" column using regular expressions
    df["yp_star_ratings"] = df["yp_star_ratings"].str.extract(r"(\d+\.\d+)")
    
    # convert "tripadvisor_rating" and "yp_star_ratings" column to float type
    df[["tripadvisor_rating", "yp_star_ratings"]] = df[
        ["tripadvisor_rating", "yp_star_ratings"]
    ].astype(float)
    
    #fill missing values in "yp_number_ofrating" with 0 and convert to integer type
    df["yp_number_ofratings"] = df["yp_number_ofratings"].fillna(0).astype(int)

    #return the processed dataframe
    return df

