import matplotlib.pyplot as plt
import pandas as pd
import read_data

data = pd.read_csv("C:\Python Projects\\time series\output-data\\factory-data.csv")

read_data.monthly_counts(data)

fig, ax = plt.subplots()