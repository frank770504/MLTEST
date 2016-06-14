# some import here
import csv

# path definition
g_csv_file_name = "order_traffic_weather.csv"

# some classed here


# main here

dbg_int_cnt = 0

with open(g_csv_file_name, 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:
    
    print ','.join(row)
    dbg_int_cnt = dbg_int_cnt + 1
    if dbg_int_cnt >= 53:
      break
