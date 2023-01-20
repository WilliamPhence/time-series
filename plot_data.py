### STANDARD LIBRARIES ###
import matplotlib.pyplot as plt
import pandas as pd
### CUSTOM FUNCTIONS ###
import read_data

data = pd.read_csv("C:\Python Projects\\time series\output-data\\factory-data.csv")
damage_df = pd.DataFrame(read_data.monthly_counts(data))

print("\nTHIS IS THE START OF plot_data.py\n")




#damage_df.reset_index(inplace=True)



print(damage_df)

damage_df.plot(
        kind='bar',
        y='Defect Category',
        xticks= damage_df.index,
        )

plt.show()



print("\nTHIS IS THE END OF plot_data.py\n")
