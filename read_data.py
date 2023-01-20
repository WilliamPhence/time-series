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
        
    print("\nSTARTING DATA FRAME:\n")
    print(df)
    print("\nFollowing dfs are proccessed\n")

    # filter data
    damage_filt = df['Defect Category'] == 'damage'
    damage_df = df[damage_filt]
    damage_df = pd.DataFrame(damage_df)
    print("DATA FRAME FILTEREED FOR ONLY DAMAGE DEFECTS\n")
    print(damage_df)

    # reduced filtered df to only relevant columns    
    damage_df = damage_df[['Date', 'Defect Category','Defect ref']]

    damage_df['year'] = damage_df['Date'].dt.year
    damage_df['month'] = damage_df['Date'].dt.month
    damage_df['day'] = damage_df['Date'].dt.day

    damage_df = damage_df[['year', 'month', 'Defect Category','Defect ref']]

    # Create year and month columnto use as indicies later
    print("DATA FRAME w/ reduced columns\n")
    print(damage_df)

    # group by month-year
    damage_df = damage_df['Defect Category'].groupby([damage_df['year'], damage_df['month']]).agg('count')
    print("DATA FRAME post grouping\n")
    print(damage_df)
    print("\nTHIS IS THE END OF read_data.py\n")

    return damage_df