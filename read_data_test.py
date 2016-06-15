# some import here
import csv
import numpy as np

# path definition
g_csv_file_name = "order_traffic_weather.csv"
dbg_int_cnt = 0
cnt_arr = np.zeros(13)
area_arr = np.array([])
# some classed here

# functions here
def WriteAreaCSV(name, area_arr):
  with open(name, 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in area_arr:
      spamwriter.writerow(row)
  print "write {} ok !".format(name)

# main here
with open(g_csv_file_name, 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in spamreader:
    for i in range(0,12):
      if row[i] == 'NULL':
        cnt_arr[i] = cnt_arr[i] + 1
    if row[2] == '1':
      row_np = np.array(row)
      area_arr = np.vstack([area_arr, row]) if area_arr.size>0 else row_np
    dbg_int_cnt = dbg_int_cnt + 1

WriteAreaCSV('area1.csv', area_arr)
