import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

rainfall_data = pd.read_csv("Rainfall_data.csv")

print(rainfall_data.head())
print(f"\n")

print(rainfall_data.describe())
print(f"\n")

print(type(rainfall_data))
print(f"\n")

print(rainfall_data.info())
print(rainfall_data.columns)
print(rainfall_data.shape)

rainfall_data["Date"] = pd.to_datetime(rainfall_data[["Year", "Month", "Day"]])
rainfall_data.set_index("Date", inplace=True)
rainfall_data = rainfall_data.drop(columns=["Year", "Month", "Day"])

fig, axes = plt.subplots(2, 2)

rainfall_data["Specific Humidity"].plot(ax=axes[0, 0], title="Specific Humidity")
rainfall_data["Relative Humidity"].plot(ax=axes[1, 0], title="Relative Humidity")
rainfall_data["Temperature"].plot(ax=axes[0, 1], title="Temperature")
rainfall_data["Precipitation"].plot(ax=axes[1,1], title="Precipitation")

plt.show()

Mumbai = rainfall_data["Precipitation"]
Mumbai.index.freq = 'MS'
print(Mumbai.head())

Mumbai.plot(title = "Precipitation")
plt.show()

seasonal_decompose(Mumbai, model = "additive").plot()
plt.show()

