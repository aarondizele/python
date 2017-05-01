import csv
from datetime import datetime

path = "google_stock_data.csv"
# file_ = open(path)
# for line in file_:
#     print(line)
# lines = [line for line in open(path)]
# # print(lines[0])
# data_ = lines[0].strip().split(',')
# for data in data_:
#     print(data, newline=" ")
# print(lines[1])


file_ = open(path, newline='')
reader = csv.reader(file_)

header = next(reader) ### print header of  file_
# data = [row for row in reader]

# print(header)
# print(data[0])
# print(data[1])

data = []
for row in reader:
    # row = [date, open, high, low, close, adj. close]
    date_ = datetime.strptime(row[0], '%m/%d/%Y')
    open_ = float(row[1])
    high_ = float(row[2])
    low_ = float(row[3])
    close_ = float(row[4])
    volume_ = int(row[5])
    adj_close_ = float(row[6])

    data.append([date_, open_, high_, low_, close_, volume_, adj_close_])

# compute and store daily stock returns

returns_path = 'google_returns.csv'
files_ = open(returns_path, 'w')
writer = csv.writer(files_)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1): ### decrement
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1] ## i++
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])
