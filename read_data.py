#### This is to practice working with time series data
####
####
####

import pandas as pd
    
def monthly_counts(df):
    # read data from file
    df = pd.DataFrame(df)

    # rename columns
    df.rename(columns={'CREATE DATE':'Date'}, inplace=True)

    # set index equal to datetime provided by data
    df['Date'] = pd.to_datetime(df['Date'], utc=True)
        
    # Create a column for year, month & day
    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month
    df['day'] = df['Date'].dt.day

    print("\nSTARTING DATA FRAME:\n")
    print(df)
    print("\nFollowing dfs are proccessed\n")

    # filter data
    damage_filt = df['Defect Category'] == 'damage'
    damage_df = df[damage_filt]
    print("DATA FRAME FILTEREED FOR ONLY DAMAGE DEFECTS\n")
    print(damage_df)

    # reduced filtered df to only relevant columns
    damage_df = damage_df[['Date','Defect Category','Defect ref', 'year', 'month']]
    damage_df = pd.DataFrame(damage_df)
    print("DATA FRAME w/ reduced columns\n")
    print(damage_df)

    # group by month-year
    damage_df = damage_df['Defect Category'].groupby([df['Date'].dt.year, df['Date'].dt.month]).agg('count')
    print("DATA FRAME post grouping\n")
    print(damage_df)

    damage_df.to_csv("C:\Python Projects\\time series\output-data\\factory-data-monthlydamage.csv")