import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\DELL\Desktop\pthon.csv",encoding="ISO-8859-1")

df.dropna(subset=["Indicator Name", "Monthly Actual", "Period Year", "Period Month"], inplace=True)

print("info of the data!!",df.info())
print("first 15 rows in the data!",df.head(15))
print("last 15 rows in the data!",df.tail(15))
print("shape of the data!",df.shape)



#grouped data
grouped = df.groupby(["Agency Name", "Indicator Name"])["Monthly Actual"].mean().reset_index()
print(grouped.head())

#filtered data data for NYC Transit and a specific indicator
filtered = df[(df["Agency Name"] == "NYC Transit") & 
              (df["Indicator Name"] == "Customer Complaints per 100000 Riders")]
print(filtered.head())

#sorting data by Monthly Actual in ascending order
sorted_data = filtered.sort_values(by="Monthly Actual", ascending=True)
print(sorted_data.head())

df['Period'] = pd.to_datetime(df['Period'], errors='coerce')
df = df.sort_values(by='Period')

#line graph
plt.figure(figsize=(15, 6))
plt.plot(df['Period'], df['Monthly Actual'], color='black', linewidth=0.5)
plt.title("Trend Analysis of Monthly Accidents")
plt.xlabel("Date")
plt.ylabel("Monthly Accidents")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
