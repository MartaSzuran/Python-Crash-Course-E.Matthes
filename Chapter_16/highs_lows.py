import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = "sitka_weather_07-2014.csv"

with open(filename) as f:
    reader = csv.reader(f)
    # function next() give one row of the file, if we will use it multiple times we will have more rows
    # reader object takes first row of the file and each of value it keep as a list element
    header_row = next(reader)
    # print(header_row)

    # better view of all headlines
    # for index, column_header in enumerate(header_row):
        # print(index, column_header)

    # take specific values
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

    print(highs)

# creating visualisation
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red")

# formatting plot
plt.title("The highest temperature on july 2014", fontsize=24)
plt.xlabel("", fontsize=16)
# fig.autofmt_xdate() create transverse labels
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
